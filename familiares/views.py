from django.shortcuts import render
from familiares.models import Familiar

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "familiares/familiares.html", {"lista_familiares": lista_familiares})
