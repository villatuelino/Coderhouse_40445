from django import forms
from django.http import request

from .models import Venta


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ["vendedor", "producto", "cantidad"]

        widgets = {
            "vendedor": forms.TextInput(attrs={"class": "form-control", "placeholder": "usuario"}),
        }
