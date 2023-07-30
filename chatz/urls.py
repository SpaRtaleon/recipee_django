from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",LoginView.as_view(template_name="login.html",redirect_authenticated_user="sample.html"),name="login-user"),
    path("logout/", LogoutView.as_view(), name="logout-user"),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('sample/',views.sample)

]