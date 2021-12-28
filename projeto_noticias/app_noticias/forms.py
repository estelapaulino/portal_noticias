from django import forms
from app_noticias.models import Artigo, Status
from django.contrib.auth.models import User, Permission


class ArtigoAdminForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'
        widgets = {
            'conteudo': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'resumo': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }

    def __init__(self, *args, request=None, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields['autor'].queryset = User.objects.filter(groups__name='autor')
        self.fields['revisor'].queryset = User.objects.filter(groups__name='revisor')
