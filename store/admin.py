from django.contrib import admin
from .models import Category,Customer,Product,Order,OrderItem,ShippingAddress,Contact
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Contact)


