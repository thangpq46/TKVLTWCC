from django.db import models
from datetime import date

def dateupdate():
    x=date.today().strftime("%Y-%m-%d")
    return x


class Brand(models.Model):
    brandid = models.CharField(db_column='BrandID', primary_key=True, max_length=200)  # Field name made lowercase.
    branddes = models.CharField(db_column='BrandDes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200, blank=True, null=True)  # Field name made lowercase.



class Customers(models.Model):
    customerid = models.CharField(db_column='ID', primary_key=True, max_length=200)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='BillingAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    shippingaddress = models.CharField(db_column='ShippingAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=200, blank=True, null=True)  # Field name made lowercase.



class Orderdetails(models.Model):
    detailsid = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.


class Orders(models.Model):
    orderid = models.CharField(db_column='OrderID', primary_key=True, max_length=200)  # Field name made lowercase.
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerID')  # Field name made lowercase.
    orderaddress = models.CharField(db_column='OrderAddress', max_length=500)  # Field name made lowercase.
    customeremail = models.CharField(db_column='CustomerEmail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate')  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=200)  # Field name made lowercase.


class Product(models.Model):
    productid = models.CharField(db_column='ID', primary_key=True, max_length=200)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    img = models.FileField(db_column='IMG', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate',default=dateupdate())  # Field name made lowercase.
    brandid = models.ForeignKey(Brand, models.DO_NOTHING, db_column='BrandID')  # Field name made lowercase.
