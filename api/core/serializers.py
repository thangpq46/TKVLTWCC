from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",'first_name','last_name','email')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("productcode", "name", "price", "img", "description","stock","createdate","brandname")

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ("orderid", "orderaddress", "username", "orderdate", "orderstatus")

class OrderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetails
        fields = ("orderid", "productname","img", "quantity", "price")

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("brandname", "branddes","img")

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("username", "default_address", "shippingaddress")


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("cartid", "username", "carttotal","cartnum","typecart")

class CartdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartdetails
        fields = ("productname","img", "quantity", "price","username")
