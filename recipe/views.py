from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Category,Recipe, RecipeIngredient,User,PopularRecipe,Ingredient
from django.core import serializers
from django.db.models import Q,Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .serializer.serialize import IngredientSerializer, RecipeIngredientSerializer,UserSerializer,CategorySerializer,CategoryRecipeSerializer,RecipeSerializer,popularRecipeSerializer
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

class GetCategory(APIView):
    def get(self,request):
        print(request)
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
       
        return Response(serializer.data)
class GetCat(APIView):
    def get(self,request,id):
        cat=CategorySerializer(Category.objects.get(pk=id))
        return Response(cat.data)


class getRecipeFromCategory(APIView):
    def get(self,request,id):
        print(self,'self')
        print(request,'request')
        print(id,'id')
        serializer=CategoryRecipeSerializer(Recipe.objects.filter(Q(Category=id)),many=True) 
        return Response(serializer.data)

class getRecipe(APIView):
    def get(self,request,id,recipeid):
        print(self,'self')
        print(request,'request')
        print(id,'id')
        serializer=RecipeSerializer(Recipe.objects.filter(Q(Category=recipeid)),many=True) 
        return Response(serializer.data)

class GetRecipeAll(APIView):
    def get(self,request):
        recipe=CategoryRecipeSerializer(Recipe.objects.all()[:20],many=True)
        return Response(recipe.data)
    

class GetPopularRecipe(APIView):
    def get(self,request):
        popular_recipes = PopularRecipe.objects.order_by('-likes')[:10]
        print(popular_recipes)
        popular_recipe_data = []
        for popular_recipe in popular_recipes:
            recipe_id = popular_recipe.recipe_id
            recipe = Recipe.objects.get(pk=recipe_id)
            print(f"Recipe ID: {recipe_id}")
            print(f"Recipe Image URL: {recipe.ImageUrl}")
            imgurl=str(recipe.ImageUrl)
            recipe_data = {
                "recipe_id":recipe_id,
                "recipe_name": recipe.RecipeName,
                "likes": popular_recipe.likes,
                "ImageUrl": "https://res.cloudinary.com/dxfl0ss2d/image/upload/v1/"+imgurl,  
            }
            popular_recipe_data.append(recipe_data)
        return Response(popular_recipe_data)
    
class GetIngredientsList(APIView):
    def get(self,request):
        ingredients=IngredientSerializer(Ingredient.objects.all(),many=True)
        return Response(ingredients.data)

class RecipeByFilterView(APIView):
    def get(self, request):
        queryset = Recipe.objects.all()

        name = request.query_params.get('name')
        ingredients = request.query_params.get('ingredient')
        categories = request.query_params.get('category')

        if name:
            queryset = queryset.filter(RecipeName__icontains=name)

        if ingredients:
            ingredient_names = ingredients.split(',')
            queryset = queryset.annotate(
                relevance=Count('ingredients', filter=Q(ingredients__IngredientName__in=ingredient_names))
            ).filter(relevance__gt=0).order_by('-relevance')

        if categories:
            categories_names=categories.split(',')
            queryset = queryset.filter(Category__in=categories_names)

        serializer = RecipeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetRecipeByName(APIView):
    def get(self,request,title):
        serializer=CategoryRecipeSerializer(Recipe.objects.filter(Q(RecipeName__icontains=title) ),many=True)
        return Response(serializer.data)

class GetRecipeById(APIView):
    def get(self,request,recipe_id):
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            ingredients = RecipeIngredient.objects.filter(recipe=recipe)

            recipe_serializer = RecipeSerializer(recipe)
            ingredients_serializer = RecipeIngredientSerializer(ingredients, many=True)  # Serialize the RecipeIngredient objects

            response_data = {
                "recipe": recipe_serializer.data,
                "ingredients": ingredients_serializer.data
            }

            return Response(response_data)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class GetIngredientForRecipe(APIView):
    def get(self,request,recipe_id):
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            ingredients = recipe.ingredients.all()
            return HttpResponse(ingredients)
        except Recipe.DoesNotExist:
            return None

#  import jwt
# >>> encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
# >>> print(encoded)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg
# >>> jwt.decode(encoded, "secret", algorithms=["HS256"])
# {'some': 'payload'}