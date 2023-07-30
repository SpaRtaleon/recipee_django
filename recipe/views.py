from django.http import HttpResponse
from .models import Category,Recipe,User
from django.core import serializers
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializer.serialize import UserSerializer
import jwt,datetime

class Register(APIView):
    def post(self,request):
        print(request.data)
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class Login(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']

        user=User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("Email is not found !")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password !")
        
        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }

        token=jwt.encode(payload,'secretkey',algorithm='HS256')

        res=Response()
        res.set_cookie('jwt',token,httponly=True)
        res.data={
            'token':token,
          
        }


        return res
    


class UserView(APIView):
    def get(self,request):
        token=request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        try:
            payload=jwt.decode(token,'secretkey',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        
        user =User.objects.filter(id=payload['id']).first()
        serializer=UserSerializer(user)


        return Response(serializer.data)


class LogoutView(APIView):
    def post(self,request):
        res=Response()
        res.delete_cookie('jwt')
        res.data={
            'message':'success'
        }
        return res
    
def index(request):
    return HttpResponse("Hello, world. You're at the recipe index.")


def getCategories(request):
    print(request)
    data=serializers.serialize('json',Category.objects.all()) 
    return HttpResponse(data)

def getRecipeFromCategory(request,id):
    data=serializers.serialize('json',Recipe.objects.filter(Q(Category=id))) 
    return HttpResponse(data)

def getRecipeByName(request,title):
    print(title)
    data=serializers.serialize('json',Recipe.objects.filter(Q(RecipeName__unaccent__icontains=title)))
    return HttpResponse(data)


#  import jwt
# >>> encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
# >>> print(encoded)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg
# >>> jwt.decode(encoded, "secret", algorithms=["HS256"])
# {'some': 'payload'}