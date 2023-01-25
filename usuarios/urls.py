from django.urls import path
from .views import cadastro, login


urlpatterns = [
    path('login/', login, name = 'login'),
    path('cadastro/', cadastro, name = 'cadastro'),
   
]