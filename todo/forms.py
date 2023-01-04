from django import forms
from .models import Item

# form will be a class that inherits built-in django class to give it some functionality
# instead of writing it out in html we can use django to render it as a template variable
class ItemForm(forms.ModelForm):
    # must tell the form which model it will be associated with
    class Meta:
        model = Item
        fields = ['name', 'done']