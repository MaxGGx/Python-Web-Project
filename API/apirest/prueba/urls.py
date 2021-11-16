from .views import *
from django.urls import path

urlpatterns = [
	path('', ResultadosVista.as_view()),
	path('hola',inicio)
]