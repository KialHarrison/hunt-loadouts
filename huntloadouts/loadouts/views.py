from django.shortcuts import render
from django.http import HttpResponse
from .models import Gun, Loadout
from .forms import LoadoutForm


def index(request):
    guns = Gun.objects.all()
    context = {
        'guns': guns
    }
    return render(request, 'loadouts/index.html')

def create_loadout(request):
    form = LoadoutForm()
    return render(request, 'loadouts/create_loadout.html', {'form': form})