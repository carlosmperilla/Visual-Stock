import json

from django.urls import reverse
from django.core.exceptions import ValidationError

from stock.models import Stock
from stock.forms import AddStockStepOne, AddStockStepTwo, AddStockOptional

def read_column_names(principal_file):
    column_names = principal_file.readline().decode('utf-8').strip().split(',')
    principal_file.seek(0)
    return column_names

def inconsistent_columns(request, fields, data):
    errors = {}
    aux_column_names = data["column_names"].copy()
    for field in fields:
        column_name = request.POST.get(field.name)
        if not (column_name in data["column_names"]):
            errors[field.label] = [{'message': 'Las columna escogida no existe en el archivo CSV.'}]
        else:
            if column_name in aux_column_names:
                aux_column_names.remove(column_name)
            else:
                errors[field.label] = [{'message': 'Las columna escogida ya fue usada. Use otro nombre de columna.'}]
    return errors

def errorsHumanize(stock_step):
    aux_errors = stock_step.errors.as_json().replace('__all__', 'General')
    for field in stock_step:
        aux_errors = aux_errors.replace(str(field.name), str(field.label))
    return aux_errors

def validate_stock_step_two(request, data):
    if request.POST.get('second_step'):
        stock_step_two = AddStockStepTwo(request.POST)
        stock_optional = AddStockOptional(request.POST)
        if stock_step_two.is_valid() and stock_optional.is_valid():
            print("PASO AL DOS!!!!!!!!!!!!!!!")
            stock_optional_noblank = [field for field in stock_optional if field.value() != ""]
            errors = inconsistent_columns(request, [*stock_step_two, *stock_optional_noblank], data)
            if errors:
                data['errors'] = json.dumps(errors)
            else:
                stock = Stock(
                              name = request.POST["name"],
                              name_column = request.POST["name_column"],
                              price_column = request.POST["price_column"],
                              quantity_column = request.POST["quantity_column"],
                              principal_file = request.FILES["principal_file"],
                              image = request.FILES["image"],
                              user = request.user,
                              **stock_optional.cleaned_data
                            )
                try:
                    stock.save()
                    data['redirect_url'] = reverse('index')
                except ValidationError as e:
                    data['errors'] = json.dumps({'General': [{'message': e.message}]})
            return data
        
        stock_step_two_errors = errorsHumanize(stock_step_two)
        stock_optional_errors = errorsHumanize(stock_optional)
        stock_stepTwo_and_optionalErrors = json.loads(stock_step_two_errors)
        stock_stepTwo_and_optionalErrors.update(json.loads(stock_optional_errors))
        data['errors'] = json.dumps(stock_stepTwo_and_optionalErrors)

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
        stock_step_one_errors = errorsHumanize(stock_step_one)
        data = {
            'errors' : stock_step_one_errors
        }
    return data