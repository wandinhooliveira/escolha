from django.shortcuts import render
from .models import Disputa
import random
# Create your views here.


def home(request):
    remover = 0
    if request.method == "POST":

        slug = request.POST['slug']
        disputa = Disputa.objects.get(slug=slug)
        votos1 = disputa.votos1
        votos2 = disputa.votos2
        remover = disputa.id
        if  request.POST['vencedor'] == 'votos1':
            Disputa.objects.filter(slug=slug).update(votos1=votos1+1)
        if  request.POST['vencedor'] == 'votos2':
            Disputa.objects.filter(slug=slug).update(votos2=votos2+1)

    consulta = Disputa.objects.all()
    ids = []
    for id in consulta:
        ids.append(id.id)
    if remover in ids:
        ids.remove(remover)
    id = random.choice(ids)
    disputa = Disputa.objects.get(id=id)

    return render(request, 'index.html', {'disputa':disputa})

def slug(request, slug):
    disputa = Disputa.objects.get(slug=slug)
    return render(request, 'index.html', {'disputa':disputa})

def results(request):
    disputalist = Disputa.objects.all()
    return render(request, 'resultadoslista.html', {'disputalist':disputalist})