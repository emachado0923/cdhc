from django import forms

from Facebook_API.models import Formularios


class GoogleForms(forms.ModelForm):
    class Meta:
        model = Formularios
        fields = ['nombreFormulario', 'urlFormulario', 'urlRespuestas','descripcion']



