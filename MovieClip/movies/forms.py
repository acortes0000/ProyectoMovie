from django import forms

class ConsultaInformacionForm(forms.Form):
    titulo = forms.CharField(label='Título de la película')