from django.contrib.auth import authenticate,logout as logoutuser
from django.db import connection
from rest_framework.reverse import reverse
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
    cart,created = Cart.objects.get_or_create(username=username)
    user['numofproducts']=cart.numofproducts
    profilequery = Profile.objects.filter(username=username)
    if(len(profilequery)<1):
        Profile.objects.create(username=username)
    profilequery = Profile.objects.filter(username=username)
    profileseri=ProfileSerializer(profilequery,many=True,context={'request': request}).data
    user['img'] = profileseri[0]['img']
    user['phonenum']=profileseri[0]['phonenum']
    response = Response(status=status.HTTP_200_OK)
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Addtocart(request):
    pid= request.data.get('productid')   
    username= request.user
    cart = Cart.objects.get(username=username)
    connection.cursor().execute("call add_to_cart(%s, %s, %s);",[1,cart.cartid,pid])
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def CartdetailsView(request):
    username = request.user
    cart = Cart.objects.get(username=username)
    queryset = Cartdetails.objects.filter(cartid=cart)
    serializer = CartdetailsSerializer(queryset,many=True).data
    for s in serializer:
        Product.objects.get(productid=s['productid']).img
        query = Product.objects.filter(productid=s['productid'])
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
    productid = data['productid']
    operator = data['operator']
    product = Product.objects.get(productid=productid)
    cart = Cart.objects.get(username=request.user)
    detail=Cartdetails.objects.get(productid=productid,cartid=cart)
    if operator =='x':
        detail.delete()
    elif operator =='+' and detail.quantity<product.stock:
        detail.quantity+=1
        detail.save()
    elif operator =='-' and detail.quantity>1:    
        detail.quantity-=1
        detail.save()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    logoutuser(request)
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
        Orderdetails.objects.create(orderid=order,productid=item.productid,quantity=item.quantity)
    Cartdetails.objects.filter(cartid=cart).delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def NewProductView(request):
    queryset=Product.objects.raw("SELECT * FROM newproduct")  
    serializers=ProductSerializer(queryset,many=True,context={'request': request}).data
    return Response(serializers)

@api_view(['GET'])
def instockProductView(request):
    queryset=Product.objects.raw("SELECT * FROM instockproduct")
    serializers=ProductSerializer(queryset,many=True,context={'request': request}).data
    return Response(serializers)

@api_view(['GET'])
def HotProductView(request):
    queryset=Product.objects.raw("SELECT * FROM hotproducts")
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
        queryset=Orders.objects.all().order_by('-orderid')
        orders = OrdersSerializer(queryset,many=True).data
        for order in orders:
            orderid =order['orderid']
            user = User.objects.get(username=order['username'])
            order['userphonenum']=Profile.objects.get(username=user.username).phonenum
            order['username']= user.first_name + ' ' + user.last_name
            queryset= Orderdetails.objects.filter(orderid=orderid)
            details = OrderdetailsSerializer(queryset,many=True).data
            for d in details:
                query = Product.objects.filter(productid=d['productid'])
                product = ProductSerializer(query,many=True,context={'request': request}).data[0]
                d['productname']=product['name']
                d['price'] = product['price']
                d['intomoney']= d['price']*d['quantity']
                d['img']=product['img']
            order['details']=details
        return Response(orders,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        orderid = request.data.get('orderid')       #0:pending 1:confirmed 2:đã thành công -1:canceled
        order = Orders.objects.get(orderid=orderid)
        order.orderstatus+=1
        order.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        orderid = request.data.get('orderid')
        Orders.objects.filter(orderid=orderid).update(orderstatus=-1)
        return Response(status=status.HTTP_200_OK)

@api_view(['POST','DELETE','PUT'])
@permission_classes([IsAdminUser])
def productadminview(request):
    productid = request.data.get('productid')
    if request.method == 'DELETE':
        Product.objects.filter(productid=productid).delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        productcode = request.data.get('productcode')
        name = request.data.get('name')
        price = request.data.get('price')
        description = request.data.get('description')
        stock = request.data.get('stock')
        brandid = request.data.get('brandname')
        brand = Brand.objects.get(id=brandid)
        img = request.data.get('img')
        if request.method == 'PUT':
            if not Product.objects.filter(productcode=productcode).exists() and not Product.objects.filter(name=name).exists() :
                Product.objects.create(productcode=productcode, name=name,price=price, description=description,img=img, brandname=brand,stock=stock)
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_409_CONFLICT)
        if request.method == 'POST':
            if(type(img)!=str):
                temp = Profile.objects.create(username=request.user,img=img)
                Product.objects.filter(productid=productid).update(img=temp.img)
                temp.delete()
            Product.objects.filter(productid=productid).update(productcode=productcode,name=name,price=price,description=description,stock=stock,brandname=brand)
            return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def submitFeed(request):
    feedback = request.data.get('feedback')
    try:
        Feedback.objects.create(topic=feedback['topic'],title=feedback['title'],name=feedback['name'],email=feedback['email'],phone=feedback['phone'],des=feedback['des'])
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)

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
        username = request.user
        queryset =Orders.objects.filter(username= username).order_by('-orderdate')
        orders =OrdersSerializer(queryset,many=True).data
        for order in orders:
            user = User.objects.get(username=username)
            order['username'] = user.first_name+" "+user.last_name
            order['phonenum'] = Profile.objects.get(username=username).phonenum
            queryset =Orderdetails.objects.filter(orderid=order['orderid'])
            details =OrderdetailsSerializer(queryset,many=True,context={'request': request}).data 
            for d in details:
                pquery = Product.objects.filter(productid=int(d['productid']))
                product = ProductSerializer(pquery,many=True,context={'request': request}).data[0]
                d['productname'] = product['name']
                d['price'] =product['price']
                d['img']= product['img']
                d['intomoney']= product['price']*d['quantity']
            order['details'] = details
        return Response(orders)
    else:
        orderid =request.data.get('orderid')
        Orders.objects.filter(orderid=orderid).update(orderstatus=-1)
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateuser(request):
    user = request.data
    User.objects.filter(username=request.user).update(first_name=user['first_name'],last_name=user['last_name'])
    if User.objects.filter(email=user['email']).exists() and User.objects.get(username=request.user).email != user['email']:
        return Response(status=status.HTTP_409_CONFLICT)
    Profile.objects.filter(username=request.user).update(phonenum=user['phonenum'])
    if type(user['img']) == str:
        return Response(status=status.HTTP_202_ACCEPTED)
    temp =Profile.objects.create(username='temp',img=user['img'])
    temp.delete()
    Profile.objects.filter(username=user['username']).update(img=user['img'])
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def changepassword(request):
    username =request.user
    new_password = request.data.get('new_password')
    rnew_password = request.data.get('rnew_password')
    user = User.objects.get(username=username)
    if not user.check_password(request.data.get('password')):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        if not new_password == rnew_password:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        elif not validpassword(new_password):
            return Response(status=status.HTTP_412_PRECONDITION_FAILED)
    user.set_password(new_password)
    user.save()
    return Response(status=status.HTTP_202_ACCEPTED)

def dictfetchall(cursor):
    # "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@api_view(['GET'])
@permission_classes([IsAdminUser])
def dashboard(request):
    cursor = connection.cursor()
    cursor.execute("select getnumberofuser()")
    nusers= int(cursor.fetchone()[0]) 
    cursor.execute("select getnumberofproducts()")
    nproducts = int(cursor.fetchone()[0])
    cursor.execute("select getnumberoforders()")
    norders = int(cursor.fetchone()[0])
    cursor.execute("select getnumberoffeedback()")
    nfeedback = int(cursor.fetchone()[0])
    cursor.execute("select getnumberoforderspending()")
    orderspending = int(cursor.fetchone()[0])
    cursor.execute("select getnumberofproductoutofstock()")
    outofstockproducts=int(cursor.fetchone()[0])
    dashboard = { 'numorders': norders,'numusers':nusers,
        'numproducts':nproducts,
        'numfeedback':nfeedback,
        'pendingorders':orderspending,
        'poutofstocks':outofstockproducts}
    return Response(dashboard)

@api_view(['GET'])  
def Brandbycode(request,code):
    queryset=Brand.objects.filter(id=code)
    serializers=BrandSerializer(queryset,many=True,context={'request': request}).data[0]
    return Response(serializers)

@api_view(['POST','DELETE','PUT'])
@permission_classes([IsAdminUser])
def Brandedit(request):
    brandid = request.data.get('id')
    name = request.data.get('brandname')
    branddes = request.data.get('branddes')
    img = request.data.get('img')
    if request.method == 'DELETE':
        Brand.objects.filter(id=request.data.get('brandid')).delete() 
    elif request.method == 'POST':
        temp = Brand.objects.create(brandname=name,branddes=branddes,img=img)
        if(type(img)!=str):
            Brand.objects.filter(id=brandid).update(img=temp.img)
            temp.delete()
        Brand.objects.filter(id=brandid).update(brandname=name,branddes=branddes)
    elif request.method == 'PUT':
        if not Brand.objects.filter(brandname=name).exists() :  #TRUE
            Brand.objects.create(brandname=name,branddes=branddes,img=img)
        else:
            return Response(status=status.HTTP_409_CONFLICT)    
    return Response(status=status.HTTP_202_ACCEPTED)