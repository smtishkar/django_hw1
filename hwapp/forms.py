from django import forms
from .models import Thing


class AddThingPhoto(forms.Form):

    thing_name  = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Описание продукта"}))
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    # thing_added_date = forms.DateField(widget=forms.Date)
    thing_image = forms.ImageField(widget=forms.FileInput(attrs={"placeholder": "Изображение продукта"}))