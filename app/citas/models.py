from __future__ import unicode_literals
from app.informacion.models import *
from app.citas.choices import *
from django.db import models

# Create your models here.

class citas(models.Model):
	codigo = models.ForeignKey(codigo_expediente, null=False, blank=False, on_delete=models.CASCADE)
	num_cita = models.IntegerField()
	fecha_cita = models.DateField() 
	observaciones= models.CharField(max_length=250)
	proxima_cita =  models.DateField() 	
	resultados = models.CharField(max_length=250)
	autorizacion = models.BooleanField()
	tutor = models.CharField(null=True,blank=True,max_length=75)

	def __unicode__(self):
		return unicode(self.codigo)

class citas_general(models.Model):
	codigo = models.ForeignKey(codigo_expediente, null=False, blank=False, on_delete=models.CASCADE)
	aparato = models.IntegerField(choices=aparato_choices) 
	mx = models.BooleanField()
	md = models.BooleanField()
	estudiante = models.ForeignKey(Usuario,null=False, blank=False)

	def __unicode__(self):
		return unicode(self.codigo)