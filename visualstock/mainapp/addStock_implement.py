import json

from django.urls import reverse

from stock.forms import AddStockStepOne, AddStockStepTwo

def read_column_names(principal_file):
    column_names = principal_file.readline().decode('utf-8').strip().split(',')
    principal_file.seek(0)
    return column_names

def inconsistent_columns(request, fields, data):
    errors = {}
    for field in fields:
        if not (request.POST.get(field) in data["column_names"]):
            errors[field] = [{'message': 'Las columna escogida no existen en el archivo CSV.'}]
    return errors

def validate_stock_step_two(request, data):
    if request.POST.get('second_step'):
        stock_step_two = AddStockStepTwo(request.POST)
        if stock_step_two.is_valid():
            errors = inconsistent_columns(request, stock_step_two.fields, data)
            if errors:
                data['errors'] = json.dumps(errors)
            else:
                data['redirect_url'] = reverse('index')
            return data
        data['errors'] = stock_step_two.errors.as_json().replace('__all__', 'General')

        return data

def validate_stock(request):
    data = {}
    stock_step_one = AddStockStepOne(request.POST, request.FILES)
    if stock_step_one.is_valid():
        column_names = read_column_names(request.FILES['principal_file'])

        data = {
            'column_names' : column_names
        }

        validate_stock_step_two(request, data)

    else:
        print(stock_step_one.errors.as_json())
        data = {
            'errors' : stock_step_one.errors.as_json()
        }
    return data