from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def stock(request, stock_name):
    is_simplified = request.GET.get('simplified', None)
    if is_simplified=='true':
        return HttpResponse(f"Un stock: {stock_name} simplificado")

    context = {}

    return render(request, "stock/stock_prub.html", context)