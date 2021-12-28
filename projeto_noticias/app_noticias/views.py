from django.shortcuts import render
from app_noticias.models import Artigo
#from app_noticias.forms import AdicionarNoticiaForm

# Create your views here.
def index(request):
    destaque = Artigo.\
        objects.\
        filter(status__nome='Publicado', categoria__nome='Destaque').\
        order_by('-data_publicacao').\
        first()
    artigos = Artigo.objects.filter(status__nome='Publicado').exclude(id=destaque.id).order_by('-data_publicacao')
    return render(request, 'index.html', dict(artigos=artigos, destaque=destaque))


def noticia(request, id):
    artigo=Artigo.objects.get(id=id)
    return render(request, 'noticia.html', dict(artigo=artigo))



