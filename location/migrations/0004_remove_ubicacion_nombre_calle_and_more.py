# Generated by Django 5.0.2 on 2024-05-15 18:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("location", "0003_delito_ubicacion_delete_ubicaciones"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ubicacion",
            name="nombre_calle",
        ),
        migrations.AddField(
            model_name="ubicacion",
            name="nombre_colonia",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Nombre de la"
            ),
        ),
    ]
