from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView,  CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def home(request):
    return render(request, "negocio/home.html")

#def libros(request):
#    contexto = {'libros': Libro.objects.all()}
#    return render(request, 'negocio/libros.html', contexto)
#
#def clientes(request):
#
#    contexto = {'clientes': Cliente.objects.all()}
#    return render(request, 'negocio/clientes.html', contexto)
#
#def editoriales(request):
#
#    contexto = {'editoriales': Editorial.objects.all()}
#    return render(request, 'negocio/editoriales.html', contexto)


#def libroForm(request):
#    if request.method == "POST":
#        miForm = LibroForm(request.POST)
#        if  miForm.is_valid():
#            libro_nombre = miForm.cleaned_data.get("nombre")
#            libro_autor = miForm.cleaned_data.get("autor")
#            libro_anio =  miForm.cleaned_data.get("anio")
#            libro = Libro(nombre = libro_nombre, autor = libro_autor, anio = libro_anio)
#            libro.save()
#            return redirect(reverse_lazy("libros"))
#         
#    else:
#        miForm = LibroForm()
#
#    return render(request, 'negocio/libroForm.html', {"form":miForm})
#
#
#def clienteForm(request):
#    if request.method == "POST":
#        miForm = ClienteForm(request.POST)
#        if miForm.is_valid():
#            cliente_nombre = miForm.cleaned_data.get("nombre")
#            cliente_apellido = miForm.cleaned_data.get("apellido")
#            cliente_email = miForm.cleaned_data.get("email")
#            cliente = Cliente(nombre = cliente_nombre, apellido = cliente_apellido, email = cliente_email)
#            cliente.save()
#            return redirect(reverse_lazy("clientes"))
#
#    else:
#        miForm = ClienteForm()
#
#    return render(request, 'negocio/clienteForm.html', {"form":miForm})
#
#def editorialForm(request):
#    if request.method == "POST":
#        miForm = EditorialForm(request.POST)
#        if miForm.is_valid():
#            editorial_nombre = miForm.cleaned_data.get("nombre")
#            editorial_email = miForm.cleaned_data.get("email")
#            editorial = Editorial(nombre = editorial_nombre, email = editorial_email)
#            editorial.save()
#            return redirect(reverse_lazy("editoriales"))
#        
#    else:
#        miForm = EditorialForm()
#
#    return render(request, 'negocio/editorialForm.html', {"form":miForm})

@login_required
def buscar(request):
    return render(request, 'negocio/buscar.html')

@login_required
def buscarLibros(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        libros = Libro.objects.filter(nombre__icontains=patron)
        contexto = {"libros": libros}
        return render(request, 'negocio/libros.html', contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

#_______________ CREATE _______________

class LibroCreate(LoginRequiredMixin, CreateView):
    model = Libro
    fields = ['nombre', 'autor', 'anio']
    success_url = reverse_lazy("libros")

class EditorialCreate(LoginRequiredMixin, CreateView):
    model = Editorial
    fields = ['nombre', 'email']
    success_url = reverse_lazy("editoriales")

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy("clientes")

#_______________ READ _______________

class LibroList(LoginRequiredMixin, ListView):
    model = Libro

class EditorialList(LoginRequiredMixin, ListView):
    model = Editorial
    
class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

#_______________ UPDATE _______________
    
class LibroUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    fields = ['nombre', 'autor', 'anio']
    success_url = reverse_lazy("libros")

class EditorialUpdate(LoginRequiredMixin, UpdateView):
    model = Editorial
    fields = ['nombre', 'email']
    success_url = reverse_lazy("editoriales")

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy("clientes")
    
#_______________ DELETE _______________

class LibroDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy("libros")

class EditorialDelete(LoginRequiredMixin, DeleteView):
    model = Editorial
    success_url = reverse_lazy("editoriales")

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes")

#_______________ LOGIN _______________
    
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if  miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            password = miForm.cleaned_data.get("password")
            user = authenticate(request, username = usuario, password = password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('home'))
            else:
                return redirect(reverse_lazy('login'))
            
         
    else:
        miForm = AuthenticationForm()

    return render(request, 'negocio/login.html', {"form":miForm})  

#_______________ REGISTER _______________

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")            
            miForm.save()
            return redirect(reverse_lazy("home"))
        
    else:
        miForm = RegistroForm()

    return render(request, 'negocio/registro.html', {"form":miForm})


    



