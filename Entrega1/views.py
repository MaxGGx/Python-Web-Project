from django.shortcuts import render
import random

def inicio(request):
    return render(request, "inicio.html")

def segunda_vista(request):
    dic1 = random.choice(['media/ZT.png','media/MikuLogo.png'])
    return render(request, "segunda_vista.html", context = {'a1':dic1})