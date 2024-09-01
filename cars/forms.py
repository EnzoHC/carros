from django import forms
from .models import Car


class CarModelForm(forms.ModelForm):
    factory_year = forms.IntegerField(
        label="Ano de Fabricação",
        min_value=1900,  # Ajuste o valor mínimo conforme necessário
        max_value=2100,  # Ajuste o valor máximo conforme necessário
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Digite o ano"}
        ),
    )
    model_year = forms.IntegerField(
        label="Ano do Modelo",
        min_value=1900,  # Ajuste o valor mínimo conforme necessário
        max_value=2100,  # Ajuste o valor máximo conforme necessário
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Digite o ano"}
        ),
    )

    class Meta:
        model = Car
        fields = [
            "model",
            "brand",
            "factory_year",
            "model_year",
            "plate",
            "value",
            "photo",
        ]
