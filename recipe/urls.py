from django.urls import path
from django.contrib.auth import views as auth_views


from .views import getCategories,getRecipeFromCategory
from .views import Register,Login,UserView,LogoutView
urlpatterns = [
    path("recipe/", getCategories, name="getCategories"),
    path("recipe/<int:id>", getRecipeFromCategory, name="getRecipeCategories"),
    path('register',Register.as_view()),
    path('login',Login.as_view()),
    path('logout',LogoutView.as_view()),
    path('user',UserView.as_view())
    # path ('recipe/<str:title>',getRecipeByName,name="getRecipeByName")


        ]