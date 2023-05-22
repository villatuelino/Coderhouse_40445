from django import forms

# from .models import Cliente
from . import models


# class ClienteForm(forms.ModelForm):
class Cliente(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["nombre", "apellido", "nacimiento", "pais_origen_id"]
