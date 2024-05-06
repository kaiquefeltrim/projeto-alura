from django.shortcuts import redirect, render
from apps.usuarios.forms import LoginForms, RegisterForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name = form['name_login'].value()
            password = form['password_login'].value()

        user = auth.authenticate(
            request,
            username =name,
            password = password
        )
        if user is not None:
            auth.login(request,user)
            messages.success(request, f"{name} conectado com sucesso ")
            return redirect('index')
        else:
            messages.error(request, "usuario ou senha invalida")
            return redirect('login')

    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
             
            name = form["name_register"].value()
            email = form["email_register"].value()
            password = form["password_register"].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, "Nome de usuario ja existente")
                return redirect('cadastro')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email de usuario ja existente")
                return redirect('cadastro')
            
            user = User.objects.create_user(
                username= name,
                email= email,
                password= password,
            )
            user.save()
            messages.success(request, "Cadrastado com sucesso")
            return redirect('login')
        
    return render(request, "usuarios/cadastro.html",{"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Você foi desconectado com sucesso ")
    return redirect('login')