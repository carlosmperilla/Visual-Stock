from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.core.exceptions import ValidationError

from stock.models import Stock
from stock.forms import AddStockStepOne, AddStockStepTwo, AddStockOptional, DeleteStock, EditFaceStock
from .addStock_implement import validate_stock

from django.contrib.auth.hashers import check_password

from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
            if name:
                stock_to_edit.name = name
            if image:
                stock_to_edit.image = request.FILES.get("image")
            try:
                stock_to_edit.save()
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