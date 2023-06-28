from django.contrib import admin
from .models import Pelicula, InformacionPelicula

# Register your models here.
admin.site.register(Pelicula)

admin.site.register(InformacionPelicula)