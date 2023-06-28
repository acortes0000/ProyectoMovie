from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    en_uso = models.BooleanField(default=False)

class InformacionPelicula(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    sinopsis = models.TextField()
    director = models.CharField(max_length=50)
    duracion = models.CharField(max_length=10)
    fecha_estreno = models.DateField()

    def __str__(self):
        return self.pelicula.titulo