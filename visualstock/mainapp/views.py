import csv
from turtle import update

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ValidationError

from stock.models import Stock
from stock.forms import AddStockStepOne, AddStockStepTwo, AddStockOptional, DeleteStock, EditFaceStock
from .addStock_implement import validate_stock

from django.contrib.auth.hashers import check_password

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def index(request):
    
    context = {
    'title' : 'Inicio',
    'is_index' : True,
    'mode' : 0
    }

    if request.user.is_authenticated:
        context["stocks"] = Stock.objects.filter(user__pk=request.user.pk)
        context["stock_step_one"] = AddStockStepOne()
        context["stock_step_two"] = AddStockStepTwo()
        context["stock_optional"] = AddStockOptional()
        context["delete_stock"] = DeleteStock(auto_id=False)
        context["edit_stock"] = EditFaceStock(auto_id=False)

        if request.GET.get("mode"):
            context["mode"] = int(request.GET.get("mode"))

    return render(request, 'mainapp/index.html', context)

@login_required
def addStock(request):
    if request.method == 'POST':
        data = validate_stock(request)
        return JsonResponse(data)

@login_required
def editStock(request):
    if request.method == 'POST':
        edit_stock = EditFaceStock(request.POST, request.FILES)
        if edit_stock.is_valid():
            stock_id = request.POST.get("stock_id")
            stock_to_edit = get_object_or_404(Stock, id=stock_id)
            previous_name = stock_to_edit.name
            name = request.POST.get("name")
            image = request.FILES.get("image")
            update_fields = []
            if name:
                stock_to_edit.name = name
                update_fields.append('name')
            if image:
                stock_to_edit.image = request.FILES.get("image")
                update_fields.append('image')
            try:
                stock_to_edit.save(update_fields=update_fields)
                messages.success(request, f"Editado correctamente: {previous_name} ===> {stock_to_edit.name}")
            except ValidationError as e:
                messages.error(request, e.message)
        else:
            messages.error(request, "Edición incorrecta, vuelva a intentarlo.")
        index_edit_mode = reverse('index')+'?mode=1'
        return redirect(index_edit_mode)


@login_required
def deleteStock(request):
    if request.method == 'POST':
        delete_stock = DeleteStock(request.POST)
        if delete_stock.is_valid():
            password = request.POST.get("password")
            if check_password(password, request.user.password):
                stock_id = request.POST.get("stock_id")
                stock_to_remove = get_object_or_404(Stock, id=stock_id)
                stock_name = stock_to_remove.name
                stock_to_remove.delete()
                messages.warning(request, f"Stock {stock_name} eliminado correctamente!")
            else:
                messages.error(request, "Contraseña incorrecta!")

        index_delete_mode = reverse('index')+'?mode=2'
        return redirect(index_delete_mode)

@login_required
def stock_to_csv(request, stock_name):
    stocks = Stock.objects.filter(user__pk=request.user.pk)
    stock_by_name = get_object_or_404(stocks, name=stock_name)
    category = bool(stock_by_name.category_column)*stock_by_name.category_column+(not bool(stock_by_name.category_column))*"Categoria"

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="{stock_name}-{timezone.now().date()}.csv"'},
    )

    writer = csv.writer(response)

    titles =  [stock_by_name.name_column, 
                    stock_by_name.price_column, 
                    stock_by_name.quantity_column, 
                    "Disponible", 
                    category,
                    stock_by_name.added_date_column, 
                    stock_by_name.updated_date_column] + stock_by_name.additional_column_as_list()

    writer.writerow(titles)
    products = stock_by_name.products.all()
    for product in products:
        avaliable = product.available*"✓"+(not product.available)*"X"
        writer.writerow(
                        [product.name, 
                        product.price, 
                        product.quantity, 
                        avaliable, 
                        product.category, 
                        product.added_date, 
                        product.updated_date] + product.additional_as_list()
                        )

    return response