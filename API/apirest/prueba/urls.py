from .views import *
from django.urls import path

urlpatterns = [
	path('CambiarImagen', CambiarPerfil.as_view()),
	path('', ResultadosVista.as_view()),
	path('hola',inicio),
]