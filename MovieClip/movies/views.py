from django.shortcuts import render
from .models import InformacionPelicula
from .forms import ConsultaInformacionForm

# Create your views here.
def movies(request):
    mensaje = None

    if request.method == 'POST':
        form = ConsultaInformacionForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            try:
                informacion_pelicula = InformacionPelicula.objects.get(pelicula__titulo=titulo)
                return render(request, "movies/movies.html", {'form': form, 'informacion_pelicula': informacion_pelicula})
            except InformacionPelicula.DoesNotExist:
                mensaje = "No se encontró la información de la película."

    else:
        form = ConsultaInformacionForm()

    return render(request, "movies/movies.html", {'form': form, 'mensaje': mensaje})