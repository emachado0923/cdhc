# Generated by Django 3.1.2 on 2020-11-26 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facebook_API', '0007_auto_20201123_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultados',
            name='correo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Facebook_API.user_facebook'),
        ),
    ]