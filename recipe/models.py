from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    username=models.CharField(unique=True, max_length=200)
    email=models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=200)
    password=models.CharField(max_length=255)
    active=models.BooleanField(default=0)
    # fav=models.ForeignKey('Recipe',null=True, on_delete=models.CASCADE)
    # username=None
    # USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

class Category(models.Model):
    title=models.CharField(max_length=255,unique=True)
    img=models.ImageField(upload_to='category')
    desc=models.TextField()
    active=models.BooleanField(default=0)
    # img=models.URLField(null=True)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    IngredientName=models.CharField(max_length=100,unique=True)
    IngredientImg=models.ImageField(upload_to='Ingredients',default='dwt2cui6dmgf7kn3ezem.svg')
    def __str__(self):
        return self.IngredientName
    

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



    
class Recipe(models.Model):
    RecipeName = models.CharField(max_length=255)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    Category= models.ManyToManyField(Category)
    Difficulty_Level = models.CharField(max_length=255)
    DurationTime = models.CharField(max_length=40)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    IngredientDesc = models.TextField(null=True)
    RecipeInfo = models.TextField(null=True)
    ImageUrl = models.ImageField(upload_to='RecipeImg',null=False)
    videoUrl = models.FileField(null=True,default="https://res.cloudinary.com/dxfl0ss2d/image/upload/v1695567764/media/bkrr6wgzfj8eavupcce5.svg")
    active=models.BooleanField(default=0)
    Recipe_Procedure = models.TextField(null=True)
    RecipeDesc = models.TextField(null=True)
    creatAt= models.DateTimeField(auto_now=True)
    # url=models.URLField(default="https://cdn-icons-png.flaticon.com/512/138/138572.png?w=740&t=st=1688529709~exp=1688530309~hmac=6d164b528c048db5a9443e5a0a392f9fe970687db39c133b517e14c14cf258cf",max_length=255)
    
    def __str__(self):
        return self.RecipeName
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)  # For example, "cups", "grams", etc.

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ingredient.IngredientName} for {self.recipe.RecipeName}"

class UserFavorites(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)


class PopularRecipe(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.DO_NOTHING)
    likes=models.IntegerField(default=1)

