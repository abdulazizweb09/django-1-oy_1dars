from django import forms
from .models import *

class FanForm(forms.ModelForm):
    class Meta:
        model=Fan
        fields=['name','asosiy','yonalish']

class UstozForm(forms.ModelForm):
    class Meta:
        model=Ustoz
        fields=['name','age','jins','daraja','fan']
        

class YonalishForm(forms.ModelForm):
    class Meta:
        model=Yonalish
        fields=['name','activ']
        