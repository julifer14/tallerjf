from django.forms import ModelForm
from cotxes.models import Reparacio

#Formulari de model per entrar o editar reparacions

class ReparacioForm(ModelForm):
    class Meta:
        model = Reparacio
        fields = ['cotxe', 'diaEntradaTaller', 'kilometres', 'descripcioAvaria', 'tecnicRepara', 'diaSortidaTaller']
