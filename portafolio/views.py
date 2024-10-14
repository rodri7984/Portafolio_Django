from django.shortcuts import render, get_object_or_404
from .models import Proyecto

def home(request):
    proyectos = Proyecto.objects.all()    

    return render(request, 'home.html', {'proyectos': proyectos})


# def detalle(request, proyecto_id):
#     publicacion = get_object_or_404(Proyecto, id=proyecto_id)
#     habilidades_lista = publicacion.habilidades.split(",")  # Divide la cadena de habilidades por comas
#     return render(request, 'detalle.html', {'publicacion': publicacion, 'habilidades_lista': habilidades_lista})

def detalle(request, proyecto_id):
    publicacion = get_object_or_404(Proyecto, id=proyecto_id)
    habilidades_lista = publicacion.habilidades.split(",")
    img_list = [publicacion.img.url]
    
    # Añade las otras imágenes si están presentes
    if publicacion.img2:
        img_list.append(publicacion.img2.url)
    if publicacion.img3:
        img_list.append(publicacion.img3.url)
    if publicacion.img4:
        img_list.append(publicacion.img4.url)
    if publicacion.img5:
        img_list.append(publicacion.img5.url)
    if publicacion.img6:
        img_list.append(publicacion.img6.url)

    context = {
        'publicacion': publicacion,
        'img_list': img_list,
        'habilidades_lista': habilidades_lista,
    }

    return render(request, 'detalle.html', context)