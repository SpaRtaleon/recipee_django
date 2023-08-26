from django.urls import path
from django.contrib.auth import views as auth_views


from .views import GetCat, GetIngredientForRecipe,Register,Login,UserView,LogoutView,GetCategory,RecipeByFilterView,getRecipeFromCategory,getRecipe,GetPopularRecipe,GetRecipeAll,GetRecipeByName,GetRecipeById
urlpatterns = [
    path("recipe/", GetCategory.as_view(), name="getCategories"),
    path("recipe/<int:id>", getRecipeFromCategory.as_view(), name="getRecipeCategories"),


    path("recipe/getcat/<int:id>", GetCat.as_view(), name="getCategoy"),


    path("recipe/<int:id>/<int:recipeid>", getRecipe.as_view(), name="getRecipe"),
    path("recipe/find/<str:title>", GetRecipeByName.as_view(), name="GetRecipeByName"),
    path("recipe/recipeid/<int:recipe_id>", GetRecipeById.as_view(), name="GetRecipeById"),
    path("recipe/ingre/<int:recipe_id>", GetIngredientForRecipe.as_view(), name="GetIngredientForRecipe"),
    path("recipe/all", GetRecipeAll.as_view(), name="GetRecipeAll"),
    path("recipe/popular", GetPopularRecipe.as_view(), name="getPopularRecipe"),
    path('recipeFilter/', RecipeByFilterView.as_view(), name='recipesByFilter'),# filter with name,ingredient,category//


    path('register',Register.as_view()),
    path('login',Login.as_view()),
    path('logout',LogoutView.as_view()),
    path('user',UserView.as_view())
    # path ('recipe/<str:title>',getRecipeByName,name="getRecipeByName")


        ]