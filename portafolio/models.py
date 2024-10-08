from django.db import models


class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    desc = models.CharField(max_length=400)
    habilidades = models.CharField(max_length=500,blank=True)
    img = models.ImageField()
    url = models.URLField(blank=True)
    img2 = models.ImageField(blank=True, null=True)
    img3 = models.ImageField(blank=True, null=True)
    img4 = models.ImageField(blank=True, null=True)
    img5 = models.ImageField(blank=True, null=True)
    img6 = models.ImageField(blank=True, null=True)
    
    




