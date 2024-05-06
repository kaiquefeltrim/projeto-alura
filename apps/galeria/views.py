from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from apps.galeria.models import Photography
from apps.galeria.forms import PhotographyForm


def index (request):
    if not request.user.is_authenticated:
        messages.error(request,"Faça o seu login por favor")
        return redirect('login')
    photographys = Photography.objects.order_by("photographys_date").filter(published=True)
    return render(request, 'galeria/index.html',{"cards": photographys})


def imagem (request,photo_id):
    photographys = get_object_or_404(Photography,pk=photo_id)
    return render(request, 'galeria/imagem.html', {"photographys": photographys})

def search_bar(request):
    if not request.user.is_authenticated:
        messages.error(request,"Faça o seu login por favor")
        return redirect('login')
    photographys = Photography.objects.order_by("photographys_date").filter(published=True)
    if "search" in request.GET:
        search_name = request.GET['search']
        if search_name:
            photographys = photographys.filter(name__icontains = search_name)
    return render(request,"galeria/index.html",{"cards": photographys})

def new_img(request):
    if not request.user.is_authenticated:
        messages.error(request,"Faça o seu login por favor")
        return redirect('login')
    form = PhotographyForm
    if request.method == 'POST':
        form = PhotographyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Foto cadastrada com sucessi")
            return redirect('index')
        
    return render(request,'galeria/new_img.html',{"form": form}) 

def edit(request,photo_id):
    photographyEdit = Photography.objects.get(id=photo_id)
    form = PhotographyForm(instance=photographyEdit)

    if request.method == 'POST':
        form = PhotographyForm(request.POST, request.FILES, instance=photographyEdit)
        if form.is_valid():
            form.save()
            messages.success(request, "Foto editada com sucesso")
            return redirect('index')

    return render(request,'galeria/edit.html',{'form': form, 'photo_id' : photo_id})

def delete(request,photo_id):
    photographyDel = Photography.objects.get(id=photo_id)
    photographyDel.delete()
    messages.success(request, "Foto deletada com sucesso")
    return redirect('index')

def filter(request, category):
    photography = Photography.objects.order_by("photographys_date").filter(published=True, category=category)

    return render(request, 'galeria/index.html', {"cards": photography})
    