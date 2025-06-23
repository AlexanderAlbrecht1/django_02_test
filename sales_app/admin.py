from django.contrib import admin
from .models import Customer, Bill, Product, ProductType, Order


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter=['first_name', 'last_name']
    readonly_fields=['account']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Order)

