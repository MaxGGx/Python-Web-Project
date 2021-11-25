from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import SignUpForm
from Entrega1.models import player,coleccionHeroe,card,hero
import random


# verificarUsuario
# Descripcion:
# Se le entrega request para verificar usuario, en caso de ser correcto, retorna un 1 para retornar a Dashboard.
# En caso de ser erroneo se arma un context para usarlo en el retorno y recargar la vista con la info.
def verificarUsuario(request):
    if request.method == 'POST':
        if ('usuario' in request.POST.keys()) and ('pass' in request.POST.keys()):
            user = auth.authenticate(username=request.POST['usuario'], password=request.POST['pass'])
            if user is not None and user.is_active:
                auth.login(request, user)
                return 1
        context = {'error' : 'error'}
        return context
    context = {'null': 0}
    return context

#Permite obtener un set de cartas random
def getCartas():
    cartas = list(card.objects.all())
    r_cartas = random.sample(cartas,5)
    return r_cartas

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if ('username' in request.POST.keys()) and ('password1' in request.POST.keys()) and ('password2' in request.POST.keys()) and ('email' in request.POST.keys()):
            if request.POST['password1'] == request.POST['password2']:
                if (not User.objects.filter(username = request.POST['username']).exists()) and (not player.objects.filter(Nickname = request.POST['username']).exists()):
                    user = User.objects.create_user(request.POST['username'], '', request.POST['password1'])
                    user.save()
                    user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
                    auth.login(request,user)
                    raw_password = request.POST['password1']
                    usuario = request.POST['username']
                    email = request.POST['email']
                    jugador = player()
                    jugador.Nickname = usuario
                    jugador.Password = raw_password
                    jugador.email = email
                    jugador.save()
                    return 1
        
        context = {'error' : 'error'}
        return context
    context = {'null': 0}
    return context

def obtener_cartas(request):
    usuario = request.user
    cartas_usuario = [x.ID_Hero for x in coleccionHeroe.objects.filter(ID_player = player.objects.filter(Nickname = usuario)[0].pk)]
    for x in cartas_usuario:
        print(x.imagen)
    context = {"cartas":cartas_usuario}
    return context

def winner(jugada1, jugada2):
    if (jugada1 or jugada2) is not None:
        jugada1Tipo = jugada1[0]
        jugada2Tipo = jugada2[0]
        jugada1N = jugada1[1:]
        jugada2N = jugada2[1:]
        if jugada1Tipo == jugada2Tipo:
            if jugada1N > jugada2N:
                ganador=True
            else:
                ganador=False
        elif (jugada1Tipo == "F" and jugada2Tipo == "A"):
            ganador=False
        elif (jugada1Tipo == "F" and jugada2Tipo == "N"):
            ganador=True
        elif (jugada1Tipo == "A" and jugada2Tipo == "N"):
            ganador=False
        elif (jugada1Tipo == "A" and jugada2Tipo == "F"):
            ganador=True
        elif (jugada1Tipo == "N" and jugada2Tipo == "F"):
            ganador=False
        elif (jugada1Tipo == "N" and jugada2Tipo == "A"):
            ganador=True
    return ganador

def procesarJugada(request):
    flag  = True
    if request.method == 'POST':
        puntajecpu = int(request.POST['PuntajeCPU'])
        puntajejugador = int(request.POST['PuntajeJugador'])
        CPU = request.POST['CPU']
        if (request.POST['Cartas'] == -1) or (request.POST['Cartas'] == '-1'):
            flag = False
            CPU = list(hero.objects.all())
            CPU = (random.choice(CPU)).imagen
        elif request.POST['CartaElegida'] == "NONE":
            flag = False
        cartas = getCartas()
        cartaelegida = request.POST['CartaElegida']
        cartacpu = request.POST['CartaCPU']
        personaje = request.POST['Personaje']
        if flag:
            ganador = winner(cartaelegida, cartacpu)
            if ganador:
                puntajejugador+=1
            else:
                puntajecpu+=1
        else:
            ganador="None"
        cartacpu = getCartas()[0]
        if (puntajejugador==3):
            context = "GANA JUGADOR"
        elif(puntajecpu == 3):
            context = "GANA CPU"
        else:
            context = {'PuntajeCPU':puntajecpu,'PuntajeJugador':puntajejugador,'Cartas':cartas,'CartaElegida':request.POST["CartaElegida"],'CartaCPU':cartacpu,'ganador':ganador, 'Personaje':personaje, 'CPU':CPU}
    print(context)
    return context



