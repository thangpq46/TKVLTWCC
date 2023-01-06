from rest_framework.test import APITestCase,APIRequestFactory
from rest_framework.test import force_authenticate
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from .views import *
from .models import *

class FPOS(APITestCase):
    def test_brand(self):
        response=self.client.get(reverse('brand'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class TestUser(APITestCase):
    
    def setUp(self) :
        self.factory=APIRequestFactory()
        self.view=register
        self.url=reverse("register")

    def autheticate(self):
        response=self.client.post(reverse("login"),{
            "username":"admin",
            "password":"@t04062001"
        })
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_register_nodata(self):
        data ={
            "user":{
                "username":"",
                "email":"",
                "password":"",
                "rpassword":""
            }
        }
        request = self.factory.post(self.url,data=data,format="json")
        response=self.view(request)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_register_weak_pass(self):
        data ={
            "user":{
                "username":"pqt4621",
                "email":"pqt4621@gmail.com",
                "password":"123456",
                "rpassword":"123456"
            }
        }
        request = self.factory.post(self.url,data=data,format="json")
        response=self.view(request)
        self.assertEqual(response.status_code,status.HTTP_428_PRECONDITION_REQUIRED)

    def test_register_password_not_match(self):
        data ={
            "user":{
                "username":"pqt4621",
                "email":"pqt4621@gmail.com",
                "password":"Tt462001",
                "rpassword":"Tt4620033"
            }
        }
        request = self.factory.post(self.url,data=data,format="json")
        response=self.view(request)
        self.assertEqual(response.status_code,status.HTTP_510_NOT_EXTENDED)

    def test_register_valid_data(self):
        data ={
            "user":{
                "username":"t46201",
                "email":"thangphan924@gmail.com",
                "password":"Tt04062001",
                "last_name":"John",
                "first_name":"John",
                "rpassword":"Tt04062001"
            }
        }
        request = self.factory.post(self.url,data=data,format="json")
        response=self.view(request)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_get_userdata_un_auth(self):
        response=self.client.get(reverse('user'))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_login_invalid_no_content(self):
        response=self.client.post(reverse('login'),{
            "username":"",
            "password":""
        })
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_login_invalid_username(self):
        response=self.client.post(reverse('login'),{
            "username":"adminn",
            "password":"@t04062001"
        })
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_login_invalid_password(self):
        response=self.client.post(reverse('login'),{
            "username":"t46201",
            "password":"Tt04062001"
        })
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

class TestAdminFeature(APITestCase):
    
    # def autheticate(self):
    #     user= User.objects.create(username="QT",password="1",is_superuser=True,is_staff=True)
    #     response=self.client.post(reverse("login"),{
    #         "username":user.username,
    #         "password":user.password
    #     })
    #     print("DASDAS")
    #     print(response.data)
    #     print("DASDAS")
    #     self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")

    # def test_get_dasboard_with_auth(self):
    #         self.autheticate()
    #         response=self.client.get(reverse("dashboard"))
    #         self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_provinces(self):
        response=self.client.get(reverse("get_provinces"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_dashboard_without_credentials(self):
        response=self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_get_orders_unauth(self):
        response= self.client.get(reverse("adminorderview"))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
    
    def test_manage_product(self):
        response= self.client.post(reverse("productadminview"),data={"productid":"1"})
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_watch_feedback_unauth(self):
        response= self.client.get(reverse("feedview"))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_delete_brand(self):
        data={
            "id":"1"
        }
        response= self.client.delete(reverse("Brandedit"),data=data,format="json")
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

class testProduct(APITestCase):
    def test_submitFeed(self):
        data={
            "feedback":{
                "topic":"Error",
                "title":"The product have error",
                "name":"Phan Quang Thang",
                "email":"thangphan924@gmail.com",
                "phone":"0981249264",
                "des":"I got your shit yesterday and it fucking broke",
            }
        }
        response= self.client.post(reverse("submitfeedback"),data=data,format="json")
        self.assertEqual(response.status_code,status.HTTP_202_ACCEPTED)

    def test_filter_product(self):
        data={
            "filterdata":"asdasdasdasdasdas"
        }
        response= self.client.post(reverse("productfilter"),data=data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)