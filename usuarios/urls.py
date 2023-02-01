from django.urls import path
from .views import cadastro, login, valida_cadastro


urlpatterns = [
    path('login/', login, name = 'login'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('valida_cadastro/', valida_cadastro, name = 'valida_cadastro' )
   
]