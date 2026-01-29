from django import forms
from .models import *

class KitobForm(forms.ModelForm):
    # name=forms.CharField(max_length=250,min_length=2)
    class Meta:
        model=Muallif
        fields=['name','age','jins','quantity','tric']
    
class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=['talaba','kitob','admin','olingan_sana','qaytarish_sana']
        widgets = {
            'olingan_sana': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'qaytarish_sana': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

class KutubxonachiForm(forms.ModelForm):
    class Meta:
        modle=Kutubxonachi
        fields=['name','start','end']
        widgets = {
            'start': forms.DateInput(
                attrs={'type': 'time'}
            ),
            'end': forms.DateInput(
                attrs={'type': 'time'}
            ),
        }