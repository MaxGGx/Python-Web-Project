from django.shortcuts import render, redirect
from .funciones_aux import verificarUsuario, register, obtener_cartas
from django.contrib import auth
import random
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
import os
import glob

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
        fotos = os.listdir('./Entrega1/static/media')
        dic1 = "media/"+random.choice(fotos)
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
        fotos = os.listdir('./Entrega1/static/media')
        dic1 = "media/"+random.choice(fotos)
        context['a1'] = dic1
        form = SignUpForm()
        context['form'] = form
        return render(request, "register.html", context, )

def archivo(request):
    cartas = os.listdir('./Entrega1/static/personajes')
    cartas = [["personajes/"+x, x[:-4].replace("_"," ")] for x in cartas]
    print(cartas)
    if request.user:
        context = {'username':request.user, 'cartas':cartas}
        return render(request,"archivo.html",context)
    context = {'cartas':cartas}
    return render(request, "archivo.html", context)

@login_required(login_url="/login/")
def juego(request):
    context = obtener_cartas(request)
    context['username'] = request.user
    return render(request,"juego.html",context)
    

@login_required(login_url="/login/")
def perfil(request):
    context = {'username' : request.user}
    return render(request, "perfil.html", context)

