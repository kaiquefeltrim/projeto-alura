from django.urls import path
from apps.galeria.views import \
    index, imagem, search_bar, delete, edit, new_img, filter
 
urlpatterns = [
    path('',index, name='index'),
    path('imagem/<int:photo_id>',imagem, name='imagem'),
    path('buscar',search_bar, name="search_bar" ),
    path('new_img',new_img, name='new_img'),
    path('edit/<int:photo_id>', edit , name='edit'),
    path('delete/<int:photo_id>', delete , name='delete'),
    path('filter/<str:category>', filter, name='filter'),
]