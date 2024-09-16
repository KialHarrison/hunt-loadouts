from django.shortcuts import render
from django.http import HttpResponse
from .models import Gun


def index(request):
    guns = Gun.objects.all()
    context = {
        'guns': guns
    }
    return render(request, 'loadouts/index.html')