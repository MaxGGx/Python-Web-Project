from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import SignUpForm
from Entrega1.models import player


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

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if ('username' in request.POST.keys()) and ('password1' in request.POST.keys()) and ('password2' in request.POST.keys()) and ('email' in request.POST.keys()):
            if request.POST['password1'] == request.POST['password2']:
                if not User.objects.filter(username = request.POST['username']).exists():
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
