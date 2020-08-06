from django import forms
from .models import *


class Upload_form(forms.ModelForm):
    class Meta:
        model=Upload_img
        fields=[
            'img'
        ]