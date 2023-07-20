from django import forms
from .models import Task


class FormCreate(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['title','text']
