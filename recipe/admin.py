from django.contrib import admin

from .models import Recipe,Category,User,UserFavorites,PopularRecipe,Ingredient,RecipeIngredient




# Register your models here.
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserFavorites)
admin.site.register(PopularRecipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)