from django.db import models
from datetime import date

def dateupdate():
    x=date.today().strftime("%Y-%m-%d")
    return x


class Address(models.Model):
    username = models.CharField(unique=True, max_length=150)
    default_address = models.CharField(db_column='Default Address', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shippingaddress = models.CharField(db_column='ShippingAddress', max_length=45, blank=True, null=True)  # Field name made lowercase.


class Brand(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    brandname = models.CharField(db_column='BrandName', max_length=200)  # Field name made lowercase.
    branddes = models.CharField(db_column='BrandDes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    img = models.FileField(db_column='IMG', max_length=200, blank=True, null=True)  # Field name made lowercase.

class Cart(models.Model):
    cartid = models.AutoField(db_column='CartID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=150)
    carttotal = models.FloatField(db_column='CartTotal')  # Field name made lowercase.
    cartnum = models.CharField(db_column='Cartnum', max_length=45, blank=True, null=True)  # Field name made lowercase.
    typecart = models.CharField(max_length=45, blank=True, null=True)


class Cartdetails(models.Model):
    deltailsid = models.AutoField(db_column='DeltailsID', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=200)
    img = models.CharField(db_column='IMG', max_length=200,default='')  # Field name made lowercase.
    quantity = models.IntegerField(default=1)
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    username = models.CharField(max_length=200)


class Orderdetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID')  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=200)
    img = models.FileField(db_column='IMG', max_length=200,default='')
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.


class Orders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    orderaddress = models.CharField(db_column='OrderAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=200)
    orderdate = models.DateField(db_column='OrderDate', blank=True,default=dateupdate())  # Field name made lowercase.
    total = models.IntegerField(db_column='Total',blank=True, null=True)
    orderstatus = models.CharField(db_column='OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='ProductCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    img = models.FileField(db_column='IMG', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate',default=dateupdate())  # Field name made lowercase.
    brandname = models.ForeignKey(Brand, models.DO_NOTHING, db_column='BrandName')  # Field name made lowercase.

class Profile(models.Model):
    username = models.CharField(max_length=200)
    img = models.FileField(db_column='IMG', max_length=200,default='placeholder.png')

class Feedback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    topic = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    des = models.CharField(db_column='Des', max_length=500, blank=True, null=True)  # Field name made lowercase.