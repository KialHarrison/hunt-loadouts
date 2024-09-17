from django import forms
from django.forms import ModelForm
from . models import Loadout


class LoadoutForm(ModelForm):
    class Meta:
        model = Loadout
        fields = ['name', 'weapon_one', 'weapon_two', 'description']
        widget = {
            'name': forms.TextInput(attrs={'label': 'Loadout Name'}),
            'weapon_one': forms.Select(attrs={'label': 'Primary Weapon'}),
            'weapon_two': forms.Select(attrs={'label': 'Secondary Weapon'}),
            'description': forms.Textarea(attrs={'rows': 5})
        }
