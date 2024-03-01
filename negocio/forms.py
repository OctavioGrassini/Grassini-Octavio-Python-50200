from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length = 25, required = True)
    email = forms.EmailField(required = True)
    password1 = forms.CharField(max_length = 30, label = "Contraseña", required = True, widget = forms.PasswordInput)
    password2 = forms.CharField(max_length = 30, label = "Confirmar Contraseña", required = True, widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(required = True)
    password1 = forms.CharField(max_length = 30, label = "Nueva contraseña", required = True, widget = forms.PasswordInput)
    password2 = forms.CharField(max_length = 30, label = "Confirmar contraseña", required = True, widget = forms.PasswordInput)
    first_name = forms.CharField(max_length = 50, label = "Nombre/s", required = True)
    last_name = forms.CharField(max_length = 50, label = "Apellido/s", required = True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']