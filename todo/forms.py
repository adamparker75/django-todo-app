from django import forms
from .models import Item


# Inherits all the functionality from forms.ModelForm
class ItemForm(forms.ModelForm):
    """
    Create an inner class which gives our form some information
    about itself. Like which fields it should render how it should
    display error messages and so on.
    We define the model and which fields we want to display.
    """
    class Meta:
        model = Item
        fields = ['name', 'done']
