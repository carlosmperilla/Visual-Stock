from django.contrib import admin
from .models import Backup

# Register your models here.
class BackupAdmin(admin.ModelAdmin):
    readonly_fields = (
                        'first_date',
                        'second_date',
                        'third_date',
                      )
    list_display = (
                    '__str__',
                    'stock_name',
                    'user_name',
                    )
    search_fields = (
                    'stock__pk',
                    'stock__name',
                    'stock__user__username'
                    )
    ordering = (
                'stock__user__username',
                'stock__name',
                )
    list_filter = (
                    'stock__user__username',
                    'stock__name',
                    )

    def stock_name(self, obj):
        return f"{obj.stock.pk} - {obj.stock.name}"

    def user_name(self, obj):
        return obj.stock.user.username

    stock_name.short_description = "Pk - Stock"
    user_name.short_description = "Usuario"


# Register your models here.
admin.site.register(Backup, BackupAdmin)
