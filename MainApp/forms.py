from django import forms

from .models import Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['text']
        label = {'text': ''}

class ToppingsForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['text']
        label = {'text': ''}