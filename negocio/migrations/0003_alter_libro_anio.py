# Generated by Django 5.0.1 on 2024-02-07 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0002_rename_año_libro_anio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='anio',
            field=models.IntegerField(),
        ),
    ]
