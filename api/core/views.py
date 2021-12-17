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
    return response

@api_view(['POST'])
def register(request):
    username= request.data.get('username')
    email= request.data.get('email')
    firstname= request.data.get('firstname')
    lastname= request.data.get('lastname')
    password= request.data.get('password')
    rpassword= request.data.get('rpassword')
    if rpassword !=password:
        return Response({'status':'pass not match'})
    user = User.objects.create_user(username,email,password)
    Cart.objects.create(username=username,carttotal=0)
    return Response({'status':'success'})

@api_view(['GET'])
def ProductView(request):
    queryset=Product.objects.all()
    serializers=ProductSerializer(queryset,many=True,context={'request': request}).data
    return Response(serializers)

@api_view(['GET'])    
def ProductbycodeView(request,code):
    queryset=Product.objects.filter(productcode=code)
    serializers=ProductSerializer(queryset,many=True,context={'request': request}).data[0]
    return Response(serializers)

@api_view(['POST'])    
def Productfilter(request):
    print(request.data)
    filterdata = "%" +request.data.get('filterdata')+"%"
    try:
        queryset=Product.objects.raw('''SELECT * FROM core_product WHERE Name LIKE %s''',[filterdata])
        print(queryset)
        serializers=ProductSerializer(queryset,many=True,context={'request': request})
        print(serializers.data) 
        return Response(serializers.data)
    except:
        return Response({'status':'failed'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Addtocart(request):
    productname= request.data.get('productname')
    username= request.user.username
    queryset = Product.objects.filter(name=productname)
    serializers=ProductSerializer(queryset,many=True,context={'request': request}).data[0]
    price = float(serializers['price'])
    img = serializers['img']
    haveincart = Cartdetails.objects.filter(productname=productname,username=username)
    serializers = CartdetailsSerializer(haveincart,many=True).data
    if len(serializers)<1:
        Cartdetails.objects.create(productname=productname,price=price,username=username,img=img)
        carttotal=Cart.objects.get(username=username).carttotal+price
        Cart.objects.filter(username=username).update(carttotal=carttotal)
    return Response({'status': 'success'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def CartdetailsView(request):
    username = request.user.username
    queryset = Cartdetails.objects.filter(username=username)
    serializer = CartdetailsSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def OrdersView(request):
    queryset=Orders.objects.all()
    serializers=OrdersSerializer(queryset,many=True).data
    return Response(serializers)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userview(request):
    username= request.user.username
    queryset = User.objects.filter(username=username)
    serializers = UserSerializer(queryset,many=True)
    user =serializers.data[0]
    querycart = Cartdetails.objects.filter(username=username)
    numofproduct = len(CartdetailsSerializer(querycart,many=True).data)
    user["productincart"] = numofproduct
    # Address =Address.objects.filter(username=username)
    # Addressobj = AddressSerializer(Address,many=True).data[0]
    # user["defaultaddress"] = Addressobj
    queryset=Cart.objects.filter(username=username)
    cart=CartSerializer(queryset,many=True).data[0]
    user["cart"] = cart
    response = Response()
    response.data ={
        'user': user
    }
    return response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def changecartdetails(request):
    print(request.data)
    data = request.data.get('data')
    productname = data['productname']
    operator = data['operator']
    # productname = request.data.get('productname')
    # operator= request.data.get('operator')
    username = request.user.username
    
    if operator == 'x':
        Cartdetails.objects.filter(productname=productname, username=username).delete()
    else:
        stock = Product.objects.get(name=productname).stock
        price = Product.objects.get(name=productname).price
        quantity=Cartdetails.objects.get(productname=productname,username=username).quantity
        if operator == '+' and quantity<stock:
            Cartdetails.objects.filter(productname=productname, username=username).update(quantity=quantity+1,price=(price*(quantity+1)))
        if operator == '-'and quantity>1:
            Cartdetails.objects.filter(productname=productname, username=username).update(quantity=quantity-1,price=(price*(quantity-1)))
    queryset = Cartdetails.objects.filter(username=username)
    items= CartdetailsSerializer(queryset,many=True).data
    sum=0
    for item in items:
        sum+=item['price']
    Cart.objects.filter(username=username).update(carttotal=sum)
    return Response({'status':'success'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    return Response()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Checkout(request):
    address=request.data.get('address')
    username= request.user.username
    order= Orders.objects.create(username=username,orderstatus='pending',orderaddress=address)
    queryset = Cartdetails.objects.filter(username=username)
    items = CartdetailsSerializer(queryset,many=True).data
    for item in items:
        Orderdetails.objects.create(orderid=order.orderid,productname=item['productname'],quantity=item['quantity'],price=item['price'])
    Cartdetails.objects.filter(username=username).delete()
    Cart.objects.filter(username=username).update(carttotal=0)
    return Response({'status': 'pending'})

@api_view(['GET'])
def NewProductView(request):
    queryset=Product.objects.all().order_by('-createdate')[:8]
    serializers=ProductSerializer(queryset,many=True,context={'request': request}).data
    return Response(serializers)

@api_view(['GET'])
def instockProductView(request):
    queryset=Product.objects.all().order_by('-stock')[:8]
    serializers=ProductSerializer(queryset,many=True,context={'request': request}).data
    return Response(serializers)

@api_view(['GET'])
def HotProductView(request):
    queryset=Product.objects.exclude(stock=0).order_by('stock')[:8]
    serializers=ProductSerializer(queryset,many=True,context={'request': request}).data
    return Response(serializers)
    
@api_view(['GET'])
def BrandView(request):
    queryset=Brand.objects.all()
    serializers=BrandSerializer(queryset,many=True,context={'request': request}).data
    return Response(serializers)

@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def AdminOrderView(request):
    if request.method == 'GET':
        queryset=Orders.objects.all().order_by('-orderdate')
        orders = OrdersSerializer(queryset,many=True).data
        for order in orders:
            queryset= Orderdetails.objects.filter(orderid=order['orderid'])
            details = OrderdetailsSerializer(queryset,many=True).data
            order['details']=details
        return Response(order)
    else:
        pass