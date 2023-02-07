from django import forms

from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('catefory', 'name', 'description', 'price', 'image')
