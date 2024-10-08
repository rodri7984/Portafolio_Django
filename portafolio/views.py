from django.shortcuts import render, get_object_or_404
from .models import Proyecto

def home(request):
    proyectos = Proyecto.objects.all()    

    return render(request, 'home.html', {'proyectos': proyectos})


def detalle(request, proyecto_id):
    publicacion = get_object_or_404(Proyecto, id=proyecto_id)
    habilidades_lista = publicacion.habilidades.split(",")  # Divide la cadena de habilidades por comas
    return render(request, 'detalle.html', {'publicacion': publicacion, 'habilidades_lista': habilidades_lista})