import json

from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from stock.models import Stock
from products.models import Product

# Create your views here.
def toggle_backup(request, stock_name, backup_num):
    """
        Activate the selected backup, delete the current products, generate the products backed up.

        The backup file becomes the current one,
        they are rearranged leaving the third field free and the state prior to the backup is backed up in it.

        The dates are also rearranged and updated.
    """
    stocks = Stock.objects.filter(user__pk=request.user.pk)
    stock_by_name = get_object_or_404(stocks, name=stock_name)
    backups = stock_by_name.backup
    
    if request.method == 'GET' and request.user.username != "Invitados":
        if backup_num == 1:
            current = backups.first
            backups.first = backups.second
            backups.first_date = backups.second_date
        
        if backup_num == 2:
            current = backups.second
            
        if backup_num == 3:
            current = backups.third

        if backup_num in (1,2):
            backups.second = backups.third
            backups.second_date = backups.third_date
        
        product_list = json.loads(current.read().decode('utf-8', errors='ignore'))
            
        stock_by_name.products.all().delete()
        for product in product_list:
            product['fields']['stock'] = stock_by_name
        Product.objects.bulk_create([Product(**product['fields']) for product in product_list])

        backups.third = backups.current
        backups.third_date = timezone.now()
        backups.current = current
        backups.save()

    return redirect("stock:stock", stock_name=stock_name)