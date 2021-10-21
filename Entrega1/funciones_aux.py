from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


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
        if ('usuario' in request.POST.keys()) and ('pass' in request.POST.keys()) and ('pass1' in request.POST.keys()):
            if request.POST['pass'] == request.POST['pass']:
                if not User.objects.filter(username = request.POST['usuario']).exists():
                    user = User.objects.create_user(request.POST['usuario'], '', request.POST['pass'])
                    user.save()
                    user = auth.authenticate(username=request.POST['usuario'], password=request.POST['pass'])
                    auth.login(request,user)
                    return 1
        context = {'error' : 'error'}
        return context
    context = {'null': 0}
    return context
