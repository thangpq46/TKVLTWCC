from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customers)
admin.site.register(Orderdetails)
admin.site.register(Orders)
admin.site.register(Product)
admin.site.register(Brand)