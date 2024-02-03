from django import forms
from .models import Thing


class AddThingPhoto(forms.Form):
    things = [(f'{thing.pk}', f'id: {thing.pk} name: {thing.thing_name} price: {thing.price}')
                for thing in Thing.objects.all()]
    thing = forms.ChoiceField(choices=things)
    thing_image = forms.ImageField()