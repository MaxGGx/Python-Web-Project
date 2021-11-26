from django.db import models

# Create your models here.
class Resultados(models.Model):
	id_historial = models.AutoField(primary_key=True)
	jugada1 = models.CharField(max_length=255)
	jugada2 = models.CharField(max_length=255)
	ganador = models.CharField(max_length=255)

	def __str__(self):
		return str(self.ganador)

class Imagenes(models.Model):
	imagen = models.CharField(max_length=255)

	def __str__(self):
		return str(self.imagen)
