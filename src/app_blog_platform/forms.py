from django import forms
from .models import Tags_Level_1, Tags_Level_2, Tags_Level_3

class Tags_Level_1Form(forms.ModelForm):
    class Meta:
        model = Tags_Level_1
        fields = ['tag_name']
        widgets = {
            'tag_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nova Entrada'})
        }

class Tags_Level_2Form(forms.ModelForm):
    class Meta:
        model = Tags_Level_2
        fields = ['tag_name']
        widgets = {
            'tag_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nova Entrada'})
        }

class Tags_Level_3Form(forms.ModelForm):
    class Meta:
        model = Tags_Level_3
        fields = ['tag_name']
        widgets = {
            'tag_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nova Entrada'})
        }