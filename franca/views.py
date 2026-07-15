from django.shortcuts import render

from franca.models import Campanha,Titulos,Participacao, Curiosidades, Elenco

def index(request):
    campanhas = Campanha.objects.order_by('data')
    titulos = Titulos.objects.order_by('ano')
    participacao = Participacao.objects.order_by('ano')
    curiosidades = Curiosidades.objects.order_by('numero')
    elencos = Elenco.objects.order_by('id')
    return render(request, 'index.html', {"cards":campanhas, "conq":titulos, "part":participacao, "cur":curiosidades, "elen":elencos})