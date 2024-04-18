from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from galeria.models import Photography

def index (request):
    photographys = Photography.objects.order_by("photographys_date").filter(published=True)
    return render(request, 'galeria/index.html',{"cards": photographys})


def imagem (request,photo_id):
    photographys = get_object_or_404(Photography,pk=photo_id)
    return render(request, 'galeria/imagem.html', {"photographys": photographys})

def search_bar(request):
    photographys = Photography.objects.order_by("photographys_date").filter(published=True)
    if "search" in request.GET:
        search_name = request.GET['search']
        if search_name:
            photographys = photographys.filter(name__icontains = search_name)
    return render(request,"galeria/search.html",{"cards": photographys})
