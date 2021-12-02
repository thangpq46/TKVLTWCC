from django.contrib.auth import authenticate
from rest_framework.reverse import reverse
import requests
import jwt,datetime
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import *
from .serializers import *
from .models import *

class BrandView(APIView):
    def get(self, request, *args, **kwargs):
        brands = Brand.objects.all()
        serializer= BrandSerializer(brands,many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializers= BrandSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer

class CustomersViewSet(viewsets.ModelViewSet):
    queryset=Customers.objects.all()
    serializer_class= CustomersSerializer

class OrderdetailsViewSet(viewsets.ModelViewSet):
    queryset=Orderdetails.objects.all()
    serializer_class= OrderdetailsSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset=Orders.objects.all()
    serializer_class= OrdersSerializer


@api_view(['POST'])
def register(request):
    username= request.query_params['username']
    email= request.query_params['email']
    password= request.query_params['password']
    user = User.objects.create_user(username,email,password)

@api_view(['POST'])
def login(request):
    username= request.data.get('username')
    password= request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        if not User.objects.filter(username=username):
            raise exceptions.AuthenticationFailed('User does not exist')
        else:
            raise exceptions.AuthenticationFailed('Incorred password')
    serializers = UserSerializer(user)
    token_endpoint = reverse(viewname='token_obtain_pair',request=request)
    token = requests.post(token_endpoint, data=request.data).json()
    response = Response()
    response.data = {
        'access': token.get('access'),
        'refresh': token.get('refresh'),
        'username': username,
    }
    response.set_cookie('username', username)
    return response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    response = Response()
    return response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userview(request):
    queryset = User.objects.filter(username=request.user.username)
    serializers = UserSerializer(queryset,many=True)
    user =serializers.data
    response = Response()
    response.data ={
        'user': user[0]
    }
    return response