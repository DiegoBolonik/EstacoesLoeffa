from django import forms
from .models import Locais


class ProductForm(forms.ModelForm):
    class Meta:
        model = Locais
        fields = ['description', 'date', 'name', 'period']
