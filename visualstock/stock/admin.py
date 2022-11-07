from re import search
from django.contrib import admin
from .models import Stock
from products.models import Product
from backup.models import Backup

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    pass

class BackupInline(admin.TabularInline):
    model = Backup

class StockAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'user',
                    )
    search_fields = (
                    'name',
                    'user__username',
                    )
    ordering = (
                'user__username', 
                'name',
                )
    list_filter = (
                    'user__username',
                    )
    inlines = (
                ProductInline, 
                BackupInline, 
                )

# Register your models here.
admin.site.register(Stock, StockAdmin)

