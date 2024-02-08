from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    return render(request, "negocio/home.html")

def libros(request):
    contexto = {'libros': Libro.objects.all()}
    return render(request, 'negocio/libros.html', contexto)

def clientes(request):

    contexto = {'clientes': Cliente.objects.all()}
    return render(request, 'negocio/clientes.html', contexto)

def editoriales(request):

    contexto = {'editoriales': Editorial.objects.all()}
    return render(request, 'negocio/editoriales.html', contexto)


def libroForm(request):
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if  miForm.is_valid():
            libro_nombre = miForm.cleaned_data.get("nombre")
            libro_autor = miForm.cleaned_data.get("autor")
            libro_anio =  miForm.cleaned_data.get("anio")
            libro = Libro(nombre = libro_nombre, autor = libro_autor, anio = libro_anio)
            libro.save()
            return render(request, "negocio/home.html")
         
    else:
        miForm = LibroForm()

    return render(request, 'negocio/libroForm.html', {"form":miForm})

    #contexto = {'libros': Libro.objects.all()}#
    #return render(request, 'negocio/libros.html', contexto)#


def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_email = miForm.cleaned_data.get("email")
            cliente = Cliente(nombre = cliente_nombre, apellido = cliente_apellido, email = cliente_email)
            cliente.save()
            return render(request, "negocio/home.html")

    else:
        miForm = ClienteForm()

    return render(request, 'negocio/clienteForm.html', {"form":miForm})

def editorialForm(request):
    if request.method == "POST":
        miForm = EditorialForm(request.POST)
        if miForm.is_valid():
            editorial_nombre = miForm.cleaned_data.get("nombre")
            editorial_email = miForm.cleaned_data.get("email")
            editorial = Editorial(nombre = editorial_nombre, email = editorial_email)
            editorial.save()
            return render(request, "negocio/home.html")
        
    else:
        miForm = EditorialForm()

    return render(request, 'negocio/editorialForm.html', {"form":miForm})


def buscar(request):
    return render(request, 'negocio/buscar.html')

def buscarLibros(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        libros = Libro.objects.filter(nombre__icontains=patron)
        contexto = {"libros": libros}
        return render(request, 'negocio/libros.html', contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")