from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('aboutme/', aboutme, name="aboutme"),


    #_______________ CREATE _______________
    path('libro_create/', LibroCreate.as_view(), name="libro_create"),
    path('cliente_create/', ClienteCreate.as_view(), name="cliente_create"),
    path('editorial_create/', EditorialCreate.as_view(), name="editorial_create"),
    path('reserva_create/', ReservaCreate.as_view(), name="reserva_create"),
    
    #_______________ READ _______________
    path('libros/', LibroList.as_view(), name="libros"),
    path('clientes/', ClienteList.as_view(), name="clientes"),
    path('editoriales/', EditorialList.as_view(), name="editoriales"),
    path('reservas/', ReservaList.as_view(), name="reservas"),

    #_______________ UPDATE _______________
    path('libro_update/<int:pk>/', LibroUpdate.as_view(), name="libro_update"),
    path('cliente_update/<int:pk>/', ClienteUpdate.as_view(), name="cliente_update"),
    path('editorial_update/<int:pk>/', EditorialUpdate.as_view(), name="editorial_update"),
    path('reserva_update/<int:pk>/', ReservaUpdate.as_view(), name="reserva_update"),

    #_______________ DELETE _______________
    path('libro_delete/<int:pk>/', LibroDelete.as_view(), name="libro_delete"),
    path('cliente_delete/<int:pk>/', ClienteDelete.as_view(), name="cliente_delete"),
    path('editorial_delete/<int:pk>/', EditorialDelete.as_view(), name="editorial_delete"),
    path('reserva_delete/<int:pk>/', LibroDelete.as_view(), name="reserva_delete"),

    #_______________  REGISTER / LOGIN / LOGOUT / EDIT _______________
    path('registro/', register, name="registro"),
    path('login/', login_request, name="login"),    
    path('logout/', LogoutView.as_view(template_name="negocio/logout.html"), name="logout"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),    
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),    

]