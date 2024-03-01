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

def aboutme(request):
    return render(request, "negocio/aboutme.html")

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

class ReservaCreate(LoginRequiredMixin, CreateView):
    model = Reserva
    fields = ['libro', 'cliente', 'telefono', 'email']
    success_url = reverse_lazy("reservas")

#_______________ READ _______________

class LibroList(LoginRequiredMixin, ListView):
    model = Libro

class EditorialList(LoginRequiredMixin, ListView):
    model = Editorial
    
class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ReservaList(LoginRequiredMixin, ListView):
    model = Reserva

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

class ReservaUpdate(LoginRequiredMixin, UpdateView):
    model = Reserva
    fields = ['libro', 'cliente', 'telefono', 'email']
    success_url = reverse_lazy("reservas")
    
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

class ReservaDelete(LoginRequiredMixin, DeleteView):
    model = Reserva
    success_url = reverse_lazy("reservas")

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

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

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

#_______________ EDIT PROFILE _______________

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        miForm = UserEditForm(request.POST)

        if miForm.is_valid():
            informacion = miForm.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            miForm.save()

            return render(request, "negocio/home.html")
        
    else:
        miForm = UserEditForm(instance=usuario)

    return render(request, 'negocio/editar_perfil.html', {"form":miForm})


@login_required
def agregarAvatar(request):

    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)

            #_____ Borrar Avatar previo _____
            avatarPrevio = Avatar.objects.filter(user=usuario)
            if len(avatarPrevio) > 0:
                for i in range(len(avatarPrevio)):
                    avatarPrevio[i].delete()
            #_________________________________
                    
            avatar = Avatar(user=usuario, imagen=miForm.cleaned_data['imagen'])
            avatar.save()

            #_________________________________
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen

            return render(request, "negocio/home.html")
        
    else:
        miForm = AvatarForm()

    return render(request, 'negocio/agregar_avatar.html', {"form":miForm})


    



