from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("productid", "name", "price", "img", "description","stock","createdate","brandid")

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ("orderid", "customerid", "orderaddress", "customeremail", "orderdate","orderstatus")

class OrderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetails
        fields = ("detailsid", "orderid", "productid", "price", "quantity")

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ("customerid", "email", "password", "fullname", "billingaddress","shippingaddress","phone")

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("brandid", "branddes", "img")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",'first_name','last_name','email')
