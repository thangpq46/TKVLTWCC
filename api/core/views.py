from django.contrib.auth import authenticate
from rest_framework.reverse import reverse
import requests
import re
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import *
from .serializers import *
from .models import *

@api_view(['POST'])
def login(request):
    username= request.data.get('username')
    password= request.data.get('password')
    if not User.objects.filter(username=username).exists() or User.objects.filter(email=username).exists():
        raise  exceptions.AuthenticationFailed('User does not exist')
    if User.objects.filter(email=username).exists():
        username=User.objects.get(email=username).username
    user = authenticate(username=username, password=password)
    if user is None:
        raise exceptions.AuthenticationFailed({ 'error' :'Incorred password'})
    token_endpoint = reverse(viewname='token_obtain_pair',request=request)
    token = requests.post(token_endpoint, data=request.data).json()
    response = Response()
    response.data = {
        'access': token.get('access'),
        'refresh': token.get('refresh'),
        'username': username,
        'status':'Login success'
    }
    return response

def validpassword(p):
    print('---------')
    print(p)
    print('---------')
    if (len(p)<6 or len(p)>12) or not re.search("[a-z]",p) or not re.search("[0-9]",p) or not re.search("[A-Z]",p) :
        return False
    return True
    
@api_view(['POST'])
def register(request):
    print(request.data)
    user = request.data.get('user')
    username= user['username']
    email= user['email']
    firstname= user['first_name']
    lastname= user['last_name']
    password= user['password']
    rpassword= user['rpassword']
    if User.objects.filter(username=username).exists():
        return Response({'status':'user alrealdy exist'})
    elif User.objects.filter(email=email).exists():
        return Response({'status':'email alrealdy exist'})
    elif validpassword(password)== False:
        return Response({'status':'Password have length from 6-12 char.It must cointain at least 1 num, 1 lowercase and 1 uppercase.'})
    elif rpassword !=password:
        return Response({'status':'password not match'})
    else:
        user = User.objects.create_user(username,email,password)
        user.last_name = lastname
        user.first_name = firstname
        user.save()
        Cart.objects.create(username=username,carttotal=0)
        Profile.objects.create(username=username)
        return Response({'status':'register success'})

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
    queryset=Cart.objects.filter(username=username)
    cart=CartSerializer(queryset,many=True).data[0]
    user["cart"] = cart
    queryimg = Profile.objects.filter(username=username)
    try:
        profile = ProfileSerializer(queryimg,many=True,context={'request': request}).data[0]
        print("this line run smoth")
    except:
        Profile.objects.create(username=username)
        profile = ProfileSerializer(queryimg,many=True,context={'request': request}).data[0]
        print("ops it jump to this")
    print (profile['img'])
    user["img"] = profile['img']
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

@api_view(['GET','POST','DELETE'])
@permission_classes([IsAdminUser])
def AdminOrderView(request):
    if request.method == 'GET':
        queryset=Orders.objects.all().order_by('-orderdate')
        orders = OrdersSerializer(queryset,many=True).data
        for order in orders:
            queryset= Orderdetails.objects.filter(orderid=order['orderid'])
            details = OrderdetailsSerializer(queryset,many=True).data
            order['details']=details
        return Response(orders)
    elif request.method == 'POST':
        orderid = request.data.get('orderid')
        order = Orders.objects.get(orderid=orderid)
        if order.orderstatus == 'pending':
            order.orderstatus = 'confirmed'
            order.save()
        elif order.orderstatus == 'confirmed':
            order.orderstatus = 'done'
            order.save()
        return Response()
    elif request.method == 'DELETE':
        orderid = request.data.get('orderid')
        print(orderid)
        Orders.objects.filter(orderid=orderid).update(orderstatus='canceled')
        return Response({'status':'cancel success'})

@api_view(['POST'])
@permission_classes([IsAdminUser])
def productadminview(request):
    trequest = request.data.get('type')
    productcode = request.data.get('productcode')
    name = request.data.get('name')
    price = request.data.get('price')
    description = request.data.get('description')
    stock = request.data.get('stock')
    brandid = request.data.get('brandname')
    brand = Brand.objects.get(id=brandid)
    img = request.data.get('img')
    productid = request.data.get('id')
    if trequest == 'x':
        Product.objects.filter(id=productid).delete()
        return Response({'status':'delete sucessful'})
    if trequest == '+':
        if (Product.objects.filter(productcode=productcode).exists()) == False and (Product.objects.filter(name=name).exists())==False :
            Product.objects.create(productcode=productcode, name=name,price=price, description=description,img=img, brandname=brand,stock=stock)
            return Response({'status': 'success'})
        else:
            return Response({'status': 'Productcode or Productname alrealdy exist'})
    elif trequest == 'e':
        return Response({'status':'well done'})
 
@api_view(['POST'])
def submitFeed(request):
    feedback = request.data.get('feedback')
    try:
        Feedback.objects.create(topic=feedback['topic'],title=feedback['title'],name=feedback['name'],email=feedback['email'],phone=feedback['phone'],des=feedback['des'])
    except:
        return Response({'status':'An error occurred while sending data. please try again later'})
    return Response({'status':'Your feedback has been noted. Staff will be in touch shortly to respond.'})

@api_view(['GET'])
@permission_classes([IsAdminUser])
def feedbackView(request):
    queryset = Feedback.objects.all().order_by('-id')
    serializers = FeedbackSerializer(queryset,many=True)
    return Response(serializers.data)