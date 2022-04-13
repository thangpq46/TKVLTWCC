from django.urls import path,include
from .views import *
from django.conf import settings
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', register,name='register'),
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
    path('user/', userview,name='user'),
    path('cart/',CartdetailsView,name='cart'),
    path('products/', ProductView,name='products'),
    path('addtocart/',Addtocart,name='addtocart'),
    path('products/<str:code>/', ProductbycodeView,name='productbycode'),
    path('productsfilter/', Productfilter,name='productfilter'),
    path('brand/', BrandView,name='brand'),
    path('newproducts/', NewProductView,name='newproducts'),
    path('instockproducts/', instockProductView,name='instockproducts'),
    path('hotproducts/', HotProductView,name='hotproducts'),
    path('checkout/',Checkout,name='checkout'),
    path('changecartdetails/',changecartdetails,name='changecart'),
    path('adminorderview/',AdminOrderView,name='adminorderview'),
    path('productadminview/',productadminview,name='productadminview'),
    path('submitfeed/',submitFeed,name='submitfeedback'),
    path('feedview/',feedbackView,name='feedview'),
    path('userorders/',userorders,name='userorders'),
    path('updateuser/',updateuser,name='updateuser'),
    path('changepass/',changepassword,name='changepass'),
    path('get_provinces_json',get_provinces_json,name='get_provinces'),
    path('dashboard',dashboard,name='dashboard')
]