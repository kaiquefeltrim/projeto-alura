from django import forms
from apps.galeria.models import Photography

class PhotographyForm(forms.ModelForm):
    class Meta:
        model = Photography
        exclude = ['published',]
        labels = {
            'description' : 'Descrição',
            'photographys_date' : 'Data de registro ',
            'user' : 'Usuário',
            'name' : 'Nome',
            'legend' : 'Legenda',
            'category' : 'Categoria',
            'photo' : 'Foto',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'legend': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'photographys_date': forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),    
        }
