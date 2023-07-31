from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    fullname=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=200)
    password=models.CharField(max_length=255)
    username=None
    USERNAME_FIELD=email
    REQUIRED_FIELDS=[]

class Category(models.Model):
    title=models.CharField(max_length=255)
    img=models.URLField(null=True)

    def __str__(self):
        return self.title
    
class Recipe(models.Model):
    RecipeName = models.CharField(max_length=255)
    Category= models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    Difficulty_Level = models.CharField(max_length=255)
    DurationTime = models.CharField(max_length=40)
    Ingredients = models.TextField(null=True)
    IngredientDesc = models.TextField(null=True)
    RecipeInfo = models.TextField(null=True)
    ImageUrl = models.URLField(null=True)
    videoUrl = models.URLField(null=True)
    Recipe_Procedure = models.TextField(null=True)
    RecipeDesc = models.TextField(null=True)
    creatAt= models.DateTimeField(auto_now=True)
    # url=models.URLField(default="https://cdn-icons-png.flaticon.com/512/138/138572.png?w=740&t=st=1688529709~exp=1688530309~hmac=6d164b528c048db5a9443e5a0a392f9fe970687db39c133b517e14c14cf258cf",max_length=255)
    
    def __str__(self):
        return self.RecipeName
    

# class Ingredient(models.Model):
#     IngredientName=models.CharField(max_length=100)

#     def __str__(self):
#         return self.IngredientName
    

# class RecipeIngredient(models.Model):
#     recipeId=models.ForeignKey(Recipe,on_delete=models.DO_NOTHING)
#     ingredientId=models.OneToOneField(Ingredient,on_delete=models.DO_NOTHING)
#     Kilogram = "Kg"
#     Gram = "G"
#     Litre = "Ltr"
#     MilliLtre = "Ml"
#     Cup = "Cup"
#     TableSpoon="TableSpoon"
#     TeaSpoon="TeaSpoon"
#     measures = [
#         (Kilogram, "Kg"),
#         (Gram, "g"),
#         (Litre, "ltr"),
#         (MilliLtre, "ml"),
#         (Cup, "cup"),
#         (TableSpoon, "tablespoon"),
#         (TeaSpoon, "teaspoon"),
#     ]
#     measurement=models.CharField(choices=measures,default=Kilogram,max_length=100)
#     capacity =models.DecimalField(max_digits=3,decimal_places=2)


