import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from .models import Stock
from products.forms import EditProduct, ImportImages
from django.contrib import messages

from .importProductImages_implement import process_zipfile

# Create your views here.
def stock(request, stock_name):
    stocks = Stock.objects.filter(user__pk=request.user.pk)
    stock_by_name = get_object_or_404(stocks, name=stock_name)
    products_by_stock = stock_by_name.products.all()

    context = {
        'is_stock': True,
        'stocks' : stocks,
        'stock' : stock_by_name,
        'products' : products_by_stock,
        'mode' : 0
    }

    if request.GET.get("mode"):
        context["mode"] = int(request.GET.get("mode"))

        if context["mode"] == 1:
            context['form_import_images'] = ImportImages()

    return render(request, "stock/stock.html", context)

@login_required
def editProducts(request, stock_name):
    stocks = Stock.objects.filter(user__pk=request.user.pk)
    stock_by_name = get_object_or_404(stocks, name=stock_name)

    if request.method == 'POST':
        edited_rows = json.loads(request.body)

        for edited_row in edited_rows:
            try:
                product_to_edit = stock_by_name.products.get(id=edited_row["id"])
            except:
                messages.error(request, "Producto no perteneciente a stock")
                return JsonResponse({'error': "Producto no perteneciente a stock"})

            update_request = request.POST.copy()
            update_request.update(edited_row)

            edit_product = EditProduct(update_request)
            if not edit_product.is_valid():
                messages.error(request, "Producto no perteneciente a stock")
                return JsonResponse({'error': "Producto no valido"})
            
            if edited_row.get("name"):
                product_to_edit.name = edited_row["name"]
            if edited_row.get("price") != None:
                product_to_edit.price = edited_row["price"]
            if edited_row.get("quantity") != None:
                product_to_edit.quantity = edited_row["quantity"]
            if edited_row.get("category"):
                product_to_edit.category = edited_row["category"]
            
            product_to_edit.save(update_fields=['name', 'price', 'quantity', 'available', 'category'])
        else:
            if hasattr(stock_by_name, 'backup'):
                stock_by_name.backup.rotate_backup()

        return JsonResponse({'error': None})

@login_required
def importProductImages(request, stock_name):
    stocks = Stock.objects.filter(user__pk=request.user.pk)
    stock_by_name = get_object_or_404(stocks, name=stock_name)

    if request.method == 'POST':
        form_import_images = ImportImages(request.POST, request.FILES)
        if form_import_images.is_valid():
            images = {"".join(image.name.split(".")[:-1]):image for image in request.FILES.getlist('images')}
            zip = request.FILES.get('zip')
            if images:
                products_to_add_images = stock_by_name.products.filter(name__in=images.keys())
                for product in products_to_add_images:
                    product.image = images.get(product.name)
                    product.save(update_fields=['image'])
                else:
                    messages.success(request, "Imagenes importadas/actualizadas correctamente")
                    if hasattr(stock_by_name, 'backup'):
                        stock_by_name.backup.rotate_backup()
            if zip:
                process_zipfile(request, stock_by_name, zip)
        else:
            for error_field, error_text in form_import_images.errors.as_data().items():
                messages.error(request, error_text[0].message)

    return redirect("stock:stock", stock_name=stock_name)

@login_required
def deleteProducts(request, stock_name):
    stocks = Stock.objects.filter(user__pk=request.user.pk)
    stock_by_name = get_object_or_404(stocks, name=stock_name)

    if request.method == 'POST':
        ids_to_remove = json.loads(request.body)
        products_to_remove = stock_by_name.products.filter(pk__in=ids_to_remove)
        try:
            products_to_remove.delete()
        except:
            messages.error(request, "Error al eliminar los productos")
            return JsonResponse({'error': "Error al eliminar los productos"})
        finally:
            if hasattr(stock_by_name, 'backup'):
                stock_by_name.backup.rotate_backup()
        
        return JsonResponse({'error': None})