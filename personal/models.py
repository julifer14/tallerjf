from django.db import models

# Create your models here.
#Model de Tecnic
class Tecnic(models.Model):
    numSegSocial = models.CharField(max_length=15)
    nom = models.CharField(max_length=100)
    esBaixa = models.BooleanField()
    
    def __unicode__(self):
        return self.nom