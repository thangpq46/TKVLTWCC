from django.urls import path,include
from .views import *
from rest_framework import routers,request



router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomersViewSet)
router.register(r'orderdetails', OrderdetailsViewSet)
router.register(r'orders', OrdersViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('brand/', BrandView.as_view(),name='brand'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', register,name='register'),
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
    path('user/', userview,name='user'),
]
