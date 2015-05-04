from django.shortcuts import render

# Create your views here.
from .models import TempData


def list_all_TempData(request):
    objs = []
    for o in TempData.objects.all():
        objs.append(o.name)

    return render(request, 'home.html', {"objs": objs})
