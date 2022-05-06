from django import forms

from .models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        label = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}