from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('libros/', libros, name="libros"),
    path('clientes/', clientes, name="clientes"),
    path('editoriales/', editoriales, name="editoriales"),
    #
    path('libroForm/', libroForm, name="libroForm"),
    path('clienteForm/', clienteForm, name="clienteForm"),
    path('editorialForm/', editorialForm, name="editorialForm"),
    #
    path('buscar/', buscar, name="buscar"),
    path('buscarLibros/', buscarLibros, name="buscarLibros"),
]