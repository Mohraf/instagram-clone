from django.urls import path, re_path
from . import views

urlpatterns = [
  path('login', views.LoginView.as_view(), name="login"),
]