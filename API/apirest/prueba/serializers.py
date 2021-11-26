from .models import *
from rest_framework import serializers

class ResultadoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Resultados
		fields=("id_historial","jugada1","jugada2","ganador")


class ImagenSerializer(serializers.ModelSerializer):
	class Meta:
		model=Imagenes
		fields=("id","imagen")