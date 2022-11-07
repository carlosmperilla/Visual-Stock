from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    readonly_fields =  (
                        'slug',
                         'available',
                        )
    list_display = (
                    'slug',
                    'price',
                    'quantity',
                    'category',
                    'available',
                    'added_date',
                    'updated_date',
                    'stock_name',
                    'user_name',
                    )
    search_fields = (
                    'name',
                    'slug',
                    'stock__name',
                    'stock__user__username'
                    )
    ordering = (
                'stock__user__username',
                'stock__name',
                'category',
                'available',
                'slug',
                )
    list_filter = (
                    'stock__user__username',
                    'stock__name',
                    'available',
                    'category',
                    )

    def stock_name(self, obj):
        return f"{obj.stock.pk} - {obj.stock.name}"

    def user_name(self, obj):
        return obj.stock.user.username

    stock_name.short_description = "Pk - Stock"
    user_name.short_description = "Usuario"

# Register your models here.
admin.site.register(Product, ProductAdmin)