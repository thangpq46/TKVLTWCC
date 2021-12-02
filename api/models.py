# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brand(models.Model):
    brandid = models.CharField(db_column='BrandID', primary_key=True, max_length=200)  # Field name made lowercase.
    branddes = models.CharField(db_column='BrandDes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brand'


class Customers(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=200)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='BillingAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    shippingaddress = models.CharField(db_column='ShippingAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class Orderdetails(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetails'


class Orders(models.Model):
    orderid = models.CharField(db_column='OrderID', primary_key=True, max_length=200)  # Field name made lowercase.
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerID')  # Field name made lowercase.
    orderaddress = models.CharField(db_column='OrderAddress', max_length=500)  # Field name made lowercase.
    customeremail = models.CharField(db_column='CustomerEmail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate')  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Product(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=200)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate')  # Field name made lowercase.
    brandid = models.ForeignKey(Brand, models.DO_NOTHING, db_column='BrandID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'
