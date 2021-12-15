from django.contrib import admin
from .models import *
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Orderdetails)
admin.site.register(Cartdetails)
admin.site.register(Cart)
admin.site.register(Brand)
admin.site.register(Address)