# Generated by Django 3.1.2 on 2020-11-26 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facebook_API', '0010_auto_20201126_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultados',
            name='Usuario',
        ),
        migrations.AlterField(
            model_name='resultados',
            name='Tipo_Salpicadero',
            field=models.CharField(max_length=200),
        ),
    ]