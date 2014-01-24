# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from cotxes import views
#Fitxer URLS de l'aplicació cotxes
urlpatterns = patterns('',
    url(r'^llistatReparacions/$', views.llistatReparacions, name='llistatReparacions'),
    url(r'^novaReparacio/$', views.vw_reparacio, name='novaReparacio'),
    url(r'^editar_reparacio/(?P<id_reparacio>\d+)$', views.vw_reparacio, name='edita_reparacio'),
)