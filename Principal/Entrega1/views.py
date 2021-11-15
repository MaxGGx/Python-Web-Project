from django.shortcuts import render, redirect
from .funciones_aux import verificarUsuario, register
from django.contrib import auth
import random
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def inicio(request):
    if request.user:
        context = {'username' : request.user}
        return render(request, "inicio.html", context)
    return render(request, "inicio.html")

def segunda_vista(request):
    context = verificarUsuario(request)
    if context == 1:
        return redirect("/", context)
    else:
        dic1 = random.choice(['media/ZT.png','media/MikuLogo.png', 'media/MakiOzePerfil.png', 'media/EntomaOverlord.png', 'media/AinzOverlord.png', 'media/gif1.gif', 'media/BMO.gif'])
        context['a1'] = dic1
        return render(request, "segunda_vista.html", context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def registro(request):
    context = register(request)
    if context == 1:
        return redirect("/", context)
    else:
        dic1 = random.choice(['media/ZT.png','media/MikuLogo.png', 'media/MakiOzePerfil.png', 'media/EntomaOverlord.png', 'media/AinzOverlord.png', 'media/gif1.gif', 'media/BMO.gif'])
        context['a1'] = dic1
        form = SignUpForm()
        context['form'] = form
        return render(request, "register.html", context, )

@login_required(login_url="/login/")
def perfil(request):
    context = {'username' : request.user}
    return render(request, "perfil.html", context)
