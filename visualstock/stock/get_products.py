from django.core.exceptions import ValidationError

from products.models import Product

import csv, codecs

def put_dates(instance, row, data):
    """
        Update the dictionary with the dates.
    """
    if row.get(instance.added_date_column):
        data["added_date"] = row.get(instance.added_date_column)
    if row.get(instance.updated_date_column):
        data["updated_date"] = row.get(instance.updated_date_column)

def put_additional_column(instance, row, data):
    """
        Updates the dictionary with the additional columns in a field.
    """
    additional_column = instance.additional_column
    if additional_column:
        additional_list = []
        for key in additional_column.split(","):
            additional_list.append(row.get(key, ""))
        data["additional"] = ",".join(additional_list)

def get_data(row, instance):
    """
        Gets the row information and assigns its corresponding stock.
    """
    data = {
                'name' : row.get(instance.name_column, ""),
                'price' : row.get(instance.price_column, ""),
                'quantity' : row.get(instance.quantity_column, ""),
                'category' : row.get(instance.category_column, ""),
            }

    put_dates(instance, row, data)
    put_additional_column(instance, row, data)
    data["stock"] = instance
    
    return data

def get_and_save_products(instance):
    """
        It gets the information of the rows and for each row it generates a product. If they have the correct format.
    """
    decode_file = codecs.iterdecode(instance.principal_file, 'utf-8')
    reader = csv.DictReader(decode_file)

    try:
        for row in reader:
            data = get_data(row, instance)
            product_by_stock = Product(**data)
            product_by_stock.save()
    except Exception as e:
        print(e)
        import traceback
        traceback.print_exc()
        raise ValidationError(f"Formato de Stock incorrecto. Elimine {instance.name} y vuelva a cargarlo con un formato correcto.")
    finally:
        instance.principal_file.close()