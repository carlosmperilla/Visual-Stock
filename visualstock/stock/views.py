from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def stock(request, stock_name):
    is_simplified = request.GET.get('simplified', None)
    if is_simplified=='true':
        return HttpResponse(f"Un stock: {stock_name} simplificado")
    return HttpResponse(f"Un stock: {stock_name}")