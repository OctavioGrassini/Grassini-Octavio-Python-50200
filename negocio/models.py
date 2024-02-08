from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        

class Editorial(models.Model):
    nombre = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

class Libro(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    anio = models.IntegerField(verbose_name="año")

    def __str__(self):
        return f"{self.nombre} - {self.autor}"
    
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['autor']