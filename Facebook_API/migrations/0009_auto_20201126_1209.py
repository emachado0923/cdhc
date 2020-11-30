# Generated by Django 3.1.2 on 2020-11-26 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facebook_API', '0008_auto_20201126_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultados',
            name='emailSocial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Facebook_API.user_facebook'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resultados',
            name='correo',
            field=models.CharField(max_length=100),
        ),
    ]
