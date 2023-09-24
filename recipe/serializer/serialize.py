from rest_framework import serializers
from ..models import User,Category,Recipe,PopularRecipe,Ingredient,RecipeIngredient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","phoneNumber","password","active"]
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","title","img","active","desc"]
    def create(self,validated_data):
        title=validated_data.pop('title',None)
        instance=self.Meta.model(**validated_data)
        col=Category()


class CategoryRecipeSerializer(serializers.ModelSerializer):
    class Meta:     #for card /limited data 
        model=Recipe
        fields=['id','RecipeName','RecipeDesc','Category','Difficulty_Level','DurationTime','ImageUrl','active']




class IngredientSerializer(serializers.ModelSerializer):
    class Meta:                 #ingredient table with name ,id,unit
        model = Ingredient
        fields =[ 'IngredientName','IngredientImg']



class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient=IngredientSerializer()
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'unit']

class RecipeSerializer(serializers.ModelSerializer):
    Category = CategorySerializer(many=True, read_only=True)        #full recipe data
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model=Recipe
        fields=['id','RecipeName','RecipeDesc','Category','Difficulty_Level','DurationTime','ingredients','IngredientDesc','RecipeInfo','ImageUrl','videoUrl','Recipe_Procedure','creatAt','active']


class popularRecipeSerializer(serializers.ModelSerializer):         #popular Recipe
    class Meta:
        model=PopularRecipe
        fields=["recipe","likes"]

