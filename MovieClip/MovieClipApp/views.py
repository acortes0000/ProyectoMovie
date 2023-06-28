from django.shortcuts import render
from .models import Clientes
from .forms import CrearCliente

# Create your views here.
def home(request):
    if request.method == 'POST':
        forms = CrearCliente(request.POST)
        if forms.is_valid():
            data = forms.cleaned_data
            user = Clientes(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])
            user.save()
        return render(request, "MovieClipApp/home.html")
    else:
        form = CrearCliente()

    return render(request, "MovieClipApp/home.html", {'form': form})