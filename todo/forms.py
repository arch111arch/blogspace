from django import forms
from .models import Item


#create a class that inherits django functionality
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
