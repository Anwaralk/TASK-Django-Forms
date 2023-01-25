from django import forms
from .models import StoreItem


# class StoreItemForm(forms.Form):
#     name = forms.CharField(label= 'name: ')
#     description = forms.Textarea(label= 'description: ')
#     kind = forms.CharField(label= 'kind: ')         
#     price = forms.CharField(label= 'price: ')

class StoreItemForm(forms.ModelForm):
    class Meta:
        model = StoreItem 
        fields = ['name', 'description', 'kind', 'price', 'category']

