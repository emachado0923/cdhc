# Generated by Django 3.1.2 on 2020-11-27 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Facebook_API', '0013_resultados_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultados',
            old_name='Usuario',
            new_name='Usuario_id',
        ),
    ]
