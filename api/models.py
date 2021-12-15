# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    username = models.CharField(unique=True, max_length=150)
    default_address = models.CharField(db_column='Default Address', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shippingaddress = models.CharField(db_column='ShippingAddress', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class Brand(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    brandname = models.CharField(db_column='BrandName', max_length=200)  # Field name made lowercase.
    branddes = models.CharField(db_column='BrandDes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brand'


class Cart(models.Model):
    cartid = models.AutoField(db_column='CartID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=150)
    carttotal = models.FloatField(db_column='CartTotal')  # Field name made lowercase.
    cartnum = models.CharField(db_column='Cartnum', max_length=45, blank=True, null=True)  # Field name made lowercase.
    typecart = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Cartdetails(models.Model):
    deltailsid = models.AutoField(db_column='DeltailsID', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=200)  # Field name made lowercase.
    quantity = models.IntegerField()
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    username = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'cartdetails'


class Orderdetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID')  # Field name made lowercase.
    productname = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductName')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetails'


class Orders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    orderaddress = models.CharField(db_column='OrderAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=200)
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='ProductCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate')  # Field name made lowercase.
    brandname = models.ForeignKey(Brand, models.DO_NOTHING, db_column='BrandName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'
