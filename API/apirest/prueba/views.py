from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *

# Create your views here.
def inicio(request):
	return HttpResponse("FUNCIONA")

class ResultadosVista(ListAPIView):
	serializer_class=ResultadoSerializer
	def get_queryset(self):
		if self.request.method == "GET":
			jugada1 = self.request.GET.get("jugada1",None)
			jugada2 = self.request.GET.get("jugada2",None)
			if (jugada1 or jugada2) is not None:
				jugada1Tipo = jugada1[0]
				jugada2Tipo = jugada2[0]
				jugada1N = jugada1[1:]
				jugada2N = jugada2[1:]
				if jugada1Tipo == jugada2Tipo:
					if jugada1N > jugada2N:
						ganador="1"
					else:
						ganador="2"
				elif (jugada1Tipo == "F" and jugada2Tipo == "A"):
					ganador="2"
				elif (jugada1Tipo == "F" and jugada2Tipo == "N"):
					ganador="1"
				elif (jugada1Tipo == "A" and jugada2Tipo == "N"):
					ganador="2"
				elif (jugada1Tipo == "A" and jugada2Tipo == "F"):
					ganador="1"
				elif (jugada1Tipo == "N" and jugada2Tipo == "F"):
					ganador="2"
				elif (jugada1Tipo == "N" and jugada2Tipo == "A"):
					ganador="1"
				newResultados = Resultados()
				newResultados.jugada1 = jugada1
				newResultados.jugada2 = jugada2
				newResultados.ganador = ganador
				newResultados.save()
				idesita = Resultados.objects.all().order_by("-id_historial")[0].id_historial
				return Resultados.objects.filter(id_historial=idesita)
			else:
				return Resultados.objects.all()
		else:	
			return Resultados.objects.all()
