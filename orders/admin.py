from django.contrib import admin
from .models import Orders


# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'status_order')
    list_display_links = ('id', 'city')
    search_fields = ('city', 'customer', 'package')


admin.site.register(Orders, OrdersAdmin)
