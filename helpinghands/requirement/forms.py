from django import forms
from .models import requirementModel

class ProductForm(forms.ModelForm):
      
    class Meta: 
        model = requirementModel
        fields = "__all__"
        exclude = ['posted_at','admin']



