# Generated by Django 4.0.6 on 2022-08-31 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTorneo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partidos',
            name='jugador1_ausente',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='partidos',
            name='jugador2_ausente',
            field=models.BooleanField(null=True),
        ),
    ]
