from django.db import models
from datetime import date

def dateupdate():
    x=date.today().strftime("%Y-%m-%d")
    return x

class Brand(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    brandname = models.CharField(db_column='BrandName', max_length=200)  # Field name made lowercase.
    branddes = models.CharField(db_column='BrandDes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'core_brand'

class Product(models.Model):
    productid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='ProductCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    img = models.ImageField(db_column='IMG', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate',default=dateupdate())  # Field name made lowercase.
    brandname = models.ForeignKey(Brand, models.CASCADE, db_column='BrandName')  # Field name made lowercase.

    class Meta:
        db_table = 'core_product'

class Cart(models.Model):
    cartid = models.AutoField(db_column='CartID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=150)
    numofproducts = models.IntegerField(blank=True, default=0)
    total = models.FloatField(db_column='Total',default=0.0)
    cartnum = models.CharField(db_column='Cartnum', max_length=45, blank=True, null=True)  # Field name made lowercase.
    typecart = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'core_cart'


class Cartdetails(models.Model):
    deltailsid = models.AutoField(db_column='DeltailsID', primary_key=True)  # Field name made lowercase.
    cartid = models.ForeignKey(Cart, models.CASCADE, db_column='CartID',default=-1)  # Field name made lowercase.
    productcode = models.ForeignKey(Product, models.CASCADE, db_column='ProductCode',null=True) # Field name made lowercase.# Field name made lowercase.
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'core_cartdetails'


class Feedback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    topic = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    des = models.CharField(db_column='Des', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'core_feedback'


class Orders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=150)
    orderdate = models.DateField(db_column='OrderDate',default=dateupdate())  # Field name made lowercase.
    total = models.FloatField(db_column='Total',default=0.0) #  # Field name made lowercase.
    orderaddress = models.CharField(db_column='OrderAddress', max_length=3000,default='')  # Field name made lowercase.
    orderstatus = models.IntegerField(db_column='OrderStatus',default=0)  # Field name made lowercase.

    class Meta:
        db_table = 'core_orders'

class Orderdetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey(Orders, models.CASCADE, db_column='OrderID')  # Field name made lowercase.
    productcode = models.ForeignKey(Product, models.CASCADE, db_column='ProductCode',null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        db_table = 'core_orderdetails'

class Profile(models.Model):
    username = models.CharField(max_length=200)
    img = models.ImageField(db_column='IMG', max_length=200,default='placeholder.png')  # Field name made lowercase.
    defaultaddress = models.CharField(db_column='DefaultAddress', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    phonenum = models.CharField(db_column='PhoneNum', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'core_profile'