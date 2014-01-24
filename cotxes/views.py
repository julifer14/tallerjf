# -*- encoding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from cotxes.models import Cotxe, Reparacio
from cotxes.forms import ReparacioForm
from django.contrib import messages
from django.http.response import HttpResponseRedirect
# Create your views here.
#Vista home es carrega al entrar a l'arrel
def home(request):
    tots_cotxes = Cotxe.objects.filter(reparacio__diaSortidaTaller__isnull= True)
    context = {'cotxes':tots_cotxes}
    return render(request, 'cotxes/home.html', context)
#Vista per entrar o editar una reparació
def vw_reparacio(request, id_reparacio = None):
    if id_reparacio is not None:
        reparacio = get_object_or_404(Reparacio, pk=id_reparacio)
    else:
        reparacio = Reparacio()    
    if request.method == 'POST':
        
        form = ReparacioForm(request.POST, instance = reparacio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reparació introduida correctament')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Ep! Hi ha hagut un error!')
    else:
        form = ReparacioForm(instance=reparacio) 
        
    return render(request, 'cotxes/form.html', {
        'form': form,
    })
#Vista per llistat les reparacions
def llistatReparacions(request):
    reparacions = Reparacio.objects.all()
    context = {'reparacions': reparacions}
    return render(request, 'cotxes/llistat_reparacions.html', context)
