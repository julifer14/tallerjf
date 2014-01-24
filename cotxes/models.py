# -*- encoding: utf-8 -*-

from django.db import models
from personal.models import Tecnic
# Create your models here.

COLORS_COTXE = (
                ('blanc', 'blanc'),
                ('groc', 'groc'),
                ('negre', 'negre'),
                ('vermell','vermell'),
                )
#Model d'un cotxe
class Cotxe(models.Model):
    matricula = models.CharField(max_length=8, unique=True)
    nomPropietari = models.CharField(max_length=100)
    nomMarca = models.CharField(max_length=100)
    nomModel = models.CharField(max_length=100)
    color = models.CharField(max_length=7, choices=COLORS_COTXE)
    dataMatriculacio = models.DateField()
    esImportat = models.BooleanField()
    
    
    def __unicode__(self):
        return self.matricula

#Model de reparacio
class Reparacio(models.Model):
    cotxe = models.ForeignKey(Cotxe)
    diaEntradaTaller = models.DateField()
    kilometres = models.CharField(max_length=15)
    descripcioAvaria = models.CharField(max_length=100)
    tecnicRepara = models.ForeignKey(Tecnic)
    diaSortidaTaller = models.DateField(blank = True, null = True)
    
    def __unicode__(self):
        return self.descripcioAvaria