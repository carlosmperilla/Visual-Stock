from django.shortcuts import render
from django.http import JsonResponse

from stock.models import Stock
from stock.forms import AddStockStepOne, AddStockStepTwo
from .addStock_implement import validate_stock

# Create your views here.
def index(request):
    
    context = {
    'title' : 'Inicio',
    'is_index' : True
    }

    if request.user.is_authenticated:
        context["stocks"] = Stock.objects.filter(user__pk=request.user.pk)
        context["stock_step_one"] = AddStockStepOne()
        context["stock_step_two"] = AddStockStepTwo()
        if request.method == 'POST':
            data = validate_stock(request)
            return JsonResponse(data)

    return render(request, 'mainapp/index.html', context)