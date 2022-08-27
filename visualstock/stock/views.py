from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import AddStockStepOne, AddStockStepTwo
from django.contrib import messages

from django.urls import reverse

# Create your views here.
def stock(request, stock_name):
    is_simplified = request.GET.get('simplified', None)
    if is_simplified=='true':
        return HttpResponse(f"Un stock: {stock_name} simplificado")

    stock_one = AddStockStepOne()
    if request.method == 'POST':
        stock_one= AddStockStepOne(request.POST, request.FILES)
        print(request.FILES)

        print(stock_one.is_valid())

        if stock_one.is_valid():
            pass


        # stock_one.clean_principal_file()

        # print(dir(stock_one))
        # print(stock_one.data.items())
        # print(stock_one.data)
        # print(stock_one.fields)

        # if signup_form.is_valid():
        #     success_message_text = """
        #         Te has 
        #         <span class="popup__span">&nbsp;registrado</span>
        #         <span class="popup__span">&nbsp;correctamente!</span>
        #     """
        #     user = signup_form.save()
        #     messages.success(request, success_message_text)
        #     login(request, user)

        #     return redirect('index')

    context = {
        'stock_one' : stock_one,
    }

    return render(request, "stock/stock_prub.html", context)

def read_column_names(principal_file):
    column_names = principal_file.readline().decode('utf-8').strip().split(',')
    principal_file.seek(0)
    return column_names


def testing_modal(request):
    stock_one = AddStockStepOne()
    stock_two = AddStockStepTwo()
    if request.method == 'POST':
        stock_one= AddStockStepOne(request.POST, request.FILES)

        if stock_one.is_valid():
            column_names = read_column_names(request.FILES['principal_file'])
            if request.POST.get('second_step'):
                stock_two = AddStockStepTwo(request.POST)
                if stock_two.is_valid():
                    for field in stock_two.fields:
                        if not (request.POST.get(field) in column_names):
                            error = {field: [{'message': 'Las columnas escogidas no existen en el archivo CSV.'}]}
                            return JsonResponse(error)
                    data = {
                        'redirect_url': reverse('index')
                    }
                    return JsonResponse(data)
                
                data = {
                'errors' : stock_two.errors.as_json().replace('__all__', 'General')
                }
                
                return JsonResponse(data)

            
            data = {
                        'column_names' : column_names
                      }
        else:
            data = {
                'errors' : stock_one.errors.as_json()
            }
        return JsonResponse(data)

    context={
        'stock_one' : stock_one,
        'stock_two' : stock_two,
    }
    return render(request, "stock/testing_modal.html", context)