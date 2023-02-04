from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256
from django.contrib import messages , auth
from django.contrib.messages import constants
from django.contrib.auth.models import User


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html',{'status': status})


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html',{'status': status} )

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip())== 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Email ou senha não podem ficar vazios')
        return redirect('/auth/cadastro/')


    if len(senha) < 8:
        messages.add_message(request, constants.ERROR, 'Sua senha deve ter no minimo 8 caracteres ')
        return redirect('/auth/cadastro/')

    usuario = Usuario.objects.filter(email = email)

    if User.objects.filter(email = email).exists():
        messages.add_message(request, constants.ERROR, 'Já exixte usuario com esse email')
        return redirect('/auth/cadastro/')
    
    if User.objects.filter(username = nome).exists():
        messages.add_message(request, constants.ERROR, 'Já exixte usuario com esse Nome')
        return redirect('/auth/cadastro/')
    
    try: 
        print(senha)
        usuario = User.objects.create_user(username=nome, email=email, password = senha)
        usuario.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')

        return redirect('/auth/cadastro/')
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')

        return redirect('/auth/cadastro/')

def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    print(nome)
    print(senha)
    usuario = auth.authenticate(request, username = nome, password=senha)

    if not usuario : 
        messages.add_message(request, constants.WARNING, 'Email ou senha invalido')
        return redirect('/auth/login/')

    else:
        print('entrou')
        auth.login(request, usuario)
        print('estou aqui')
        return redirect('/plataforma/home/')

def sair(request):
    return HttpResponse(request.session.get_expiry_age())
    request.session.flush()
    messages.add_message(request, constants.WARNING, 'Faça login antes de acessar a plataforma')

    # return redirect('/auth/login')

