from django.contrib.auth import authenticate, get_user
from rest_framework.reverse import reverse
from django.db.models import F
import requests
from rest_framework_simplejwt import *
import re
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import *
from .serializers import *
from .models import *
import orjson
from vietnam_provinces import NESTED_DIVISIONS_JSON_PATH
from vietnam_provinces.enums import ProvinceEnum, ProvinceDEnum, DistrictEnum, DistrictDEnum
@api_view(['POST'])
def login(request):
    username= request.data.get('username')
    password= request.data.get('password')
    if username=='' or password=='':
        return  Response(status=status.HTTP_204_NO_CONTENT)
    if not User.objects.filter(username=username).exists():
        return  Response(status=status.HTTP_404_NOT_FOUND)
    if authenticate(username=username, password=password) is None:
        return  Response(status=status.HTTP_401_UNAUTHORIZED)
    token_endpoint = reverse(viewname='token_obtain_pair',request=request)
    token = requests.post(token_endpoint, data=request.data).json()
    response = Response(status=status.HTTP_200_OK)
    response.data = {
        'access': token.get('access'),
        'refresh': token.get('refresh'),
    }
    return response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userview(request):
    username= request.user
    queryset = User.objects.filter(username=username)
    user = UserSerializer(queryset,many=True).data[0]
    try:
        user['numofproducts'] = Cart.objects.get(username=username).numofproducts
    except Cart.DoesNotExist:
        Cart.objects.create(username=username,numofproducts=0,total=0.0)
        user['numofproducts'] = Cart.objects.get(username=username).numofproducts
    profilequery = Profile.objects.filter(username=username)
    try:
        user['img'] = ProfileSerializer(profilequery,many=True,context={'request': request}).data[0]['img']
    except:
        Profile.objects.create(username=username)
        user['img'] = ProfileSerializer(profilequery,many=True,context={'request': request}).data[0]['img']
    response = Response(status=status.HTTP_200_OK)
    # for provided in ProvinceEnum:
    #     print(provided.value.name)
    # province_code = '624'
    # province = DistrictEnum[f'D_{province_code}'].value
    # print(province)
    province =orjson.loads(NESTED_DIVISIONS_JSON_PATH.read_bytes())
    response.data ={
        'user': user
    }
    return response

@api_view(['GET'])
def get_provinces_json(request):
    provinces =orjson.loads(NESTED_DIVISIONS_JSON_PATH.read_bytes())
    return Response(provinces)

def validpassword(p):
    if (len(p)<6 or len(p)>12) or not re.search("[a-z]",p) or not re.search("[0-9]",p) or not re.search("[A-Z]",p) :
        return False
    return True
    
@api_view(['POST'])
def register(request):
    userdata = request.data.get('user')
    username= userdata['username']
    email= userdata['email']
    password= userdata['password']
    rpassword= userdata['rpassword']
    if username == '' or email == '' or password == '' or rpassword == '':
        return Response(status=status.HTTP_204_NO_CONTENT)
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        return Response(status=status.HTTP_409_CONFLICT)
    elif validpassword(password)== False:
        return Response(status = status.HTTP_428_PRECONDITION_REQUIRED)
    elif rpassword !=password:
        return Response(status=status.HTTP_510_NOT_EXTENDED)
    else:
        user = User.objects.create_user(username,email,password)
        user.last_name = userdata['last_name']
        user.first_name = userdata['first_name']
        user.save()
        Cart.objects.create(username=username)
        Profile.objects.create(username=username)
        return Response(status=status.HTTP_201_CREATED)

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
    filterdata = "%" +request.data.get('filterdata')+"%" # %9%
    try:
        queryset=Product.objects.raw('''SELECT * FROM core_product WHERE Name LIKE %s''',[filterdata])
        serializers=ProductSerializer(queryset,many=True,context={'request': request}) 
        return Response(serializers.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

def updateproductquantity(product,cart,operator):
    if operator == 'x':
        Cartdetails.objects.filter(productcode=product, cartid=cart).delete()
        Cart.objects.filter(cartid=cart.cartid).update(numofproducts=F('numofproducts')-1)
    elif operator == 'c':
        Cartdetails.objects.create(cartid=cart,productcode=product,quantity=1)
        Cart.objects.filter(cartid=cart.cartid).update(numofproducts=F('numofproducts')+1)
    else:
        detail= Cartdetails.objects.get(productcode=product, cartid=cart)
        if operator == '+' and detail.quantity<product.stock:
            Cartdetails.objects.filter(productcode=product, cartid=cart).update(quantity=F('quantity')+1)
            cart.total=cart.total+product.price
        if operator == '-'and detail.quantity>1:
            Cartdetails.objects.filter(productcode=product, cartid=cart).update(quantity=F('quantity')-1)
            cart.total=cart.total-product.price
        cart.save()
    return


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Addtocart(request):
    pcode= request.data.get('productcode')   
    username= request.user
    product = Product.objects.get(productcode=pcode)
    cart = Cart.objects.get(username=username)
    if len(Cartdetails.objects.filter(productcode=product,cartid=cart)) < 1: #check if exist in user's cart
        # Cartdetails.objects.create(productcode=product,cartid=cart)
        updateproductquantity(product,cart,'c')
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def CartdetailsView(request):
    username = request.user
    cart = Cart.objects.get(username=username)
    queryset = Cartdetails.objects.filter(cartid=cart)
    serializer = CartdetailsSerializer(queryset,many=True).data
    for s in serializer:
        Product.objects.get(id=s['productcode']).img
        query = Product.objects.filter(id=s['productcode'])
        product =ProductSerializer(query,many=True,context={'request': request}).data[0]
        s['productname']= product['name']
        s['img'] = product['img']
        s['price'] = s['quantity']*product['price']
    response = Response(status=status.HTTP_200_OK)
    response.data = {
        'cartdetails':serializer,
        'total':cart.total
    }
    return response

@api_view(['GET'])
def OrdersView(request):
    queryset=Orders.objects.all()
    serializers=OrdersSerializer(queryset,many=True).data
    return Response(serializers)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def changecartdetails(request):
    data = request.data.get('data')
    productcode = data['productcode']
    operator = data['operator']
    username = request.user
    product = Product.objects.get(id=productcode)
    cart = Cart.objects.get(username=username)
    updateproductquantity(product,cart,operator)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    return Response()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Checkout(request):
    address=request.data.get('address')
    username= request.user
    cart =Cart.objects.get(username=username)
    order= Orders.objects.create(username=username,orderaddress=address,total=cart.total)
    items = Cartdetails.objects.filter(cartid=cart)
    for item in items:
        Orderdetails.objects.create(orderid=order,productcode=item.productcode,quantity=item.quantity)
        Product.objects.filter(productcode=item.productcode.productcode).update(stock=F('stock')-item.quantity)
    Cartdetails.objects.filter(cartid=cart).delete()
    Cart.objects.filter(username=username).update(numofproducts=0)
    return Response(status=status.HTTP_202_ACCEPTED)

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
            orderid =order['orderid']
            user = User.objects.get(username=order['username'])
            name = user.first_name + ' ' + user.last_name
            order['username']= name
            queryset= Orderdetails.objects.filter(orderid=orderid)
            details = OrderdetailsSerializer(queryset,many=True,context={'request': request}).data
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
        Orders.objects.filter(orderid=orderid).update(orderstatus='canceled')
        return Response({'status':'cancel success'})

@api_view(['POST','DELETE','PUT'])
@permission_classes([IsAdminUser])
def productadminview(request):
    if request.method == 'DELETE':
        productid = request.data.get('productid')
        Product.objects.filter(id=productid).delete()
        return Response()
    else:
        productcode = request.data.get('productcode')
        name = request.data.get('name')
        price = request.data.get('price')
        description = request.data.get('description')
        stock = request.data.get('stock')
        brandid = request.data.get('brandname')
        brand = Brand.objects.get(id=brandid)
        img = request.data.get('img')
        productid = request.data.get('id')
        if request.method == 'PUT':
            if (Product.objects.filter(productcode=productcode).exists()) == False and (Product.objects.filter(name=name).exists())==False :
                Product.objects.create(productcode=productcode, name=name,price=price, description=description,img=img, brandname=brand,stock=stock)
                return Response()
            else:
                return Response({'status': 'Productcode or Productname alrealdy exist'})
        if request.method == 'POST':
            Product.objects.filter(id=productid).delete()
            Product.objects.create(id=productid,productcode=productcode,name=name,price=price,img=img,description=description,stock=stock,brandname=brand)
            return Response()
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


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def userorders(request):
    if request.method == 'GET':
        username = request.user.username
        queryset =Orders.objects.filter(username= username).order_by('-orderdate')
        orders =OrdersSerializer(queryset,many=True).data
        if len(orders) < 0:
            return Response()
        else:
            for order in orders:
                queryset =Orderdetails.objects.filter(orderid=order['orderid'])
                details =OrderdetailsSerializer(queryset,many=True,context={'request': request}).data 
                order['details'] = details
            return Response(orders)
    else:
        orderid =request.data.get('orderid')
        Orders.objects.filter(orderid=orderid).update(orderstatus='canceled')
        return Response({'status':'Your order has been successfully canceled'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateuser(request):
    user = request.data
    User.objects.filter(username=user['username']).update(email=user['email'],first_name=user['first_name'],last_name=user['last_name'])
    if type(user['img']) == type(''):
        return Response()
    Profile.objects.create(username='temp',img=user['img'])
    Profile.objects.filter(username='temp').delete()
    Profile.objects.filter(username=user['username']).update(img=user['img'])
    return Response()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def changepassword(request):
    print(request.data)
    username =request.user
    new_password = request.data.get('new_password')
    rnew_password = request.data.get('rnew_password')
    user = User.objects.get(username=username)
    if user.check_password(request.data.get('password')) ==False:
        return Response({'status':'Incorrect Password'})
    else:
        if not new_password == rnew_password:
            return Response({'status':'New Password not match'})
        elif not validpassword(new_password):
            return Response({'status':'Password not strong enough'})
    user.set_password(new_password)
    user.save()
    return Response({'status':'success'})