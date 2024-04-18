from django.urls import path
from galeria.views import index, imagem, search_bar

urlpatterns = [
    path('',index, name='index'),
    path('imagem/<int:photo_id>',imagem, name='imagem'),
    path('buscar',search_bar, name="search_bar" )
]