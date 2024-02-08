from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length = 25, required = True)
    apellido = forms.CharField(max_length = 25, required = True)
    email = forms.EmailField(required = True)

class EditorialForm(forms.Form):
    nombre = forms.CharField(max_length = 25, required = True)
    email = forms.EmailField(required = True)

class LibroForm(forms.Form):
    nombre = forms.CharField(max_length = 50, required = True)
    autor = forms.CharField(max_length = 50, required = True)
    anio = forms.IntegerField(required = True)

    class Meta:
        fields = [ 'nombre', 'autor', 'año' ]
