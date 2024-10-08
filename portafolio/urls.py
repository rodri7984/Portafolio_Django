from . import views
from django.urls import path

app_name = "port"

urlpatterns = [
    path("", views.home, name='home'),
    path("home/", views.home, name='home'),
    path("detalle/", views.detalle, name='detalle'),
    path("<int:proyecto_id>", views.detalle,name='detalle'),
    path("detalle/<int:proyecto_id>/", views.detalle, name="detalle"),

]