from django.shortcuts import render
from .models import Mes


def index(request):
    context = {'Mes': Mes.objects.all()}
    return render(request, 'stena/index.html', context)

