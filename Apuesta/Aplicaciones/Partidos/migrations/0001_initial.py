# Generated by Django 4.1.4 on 2022-12-18 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=50)),
                ('grupo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion', models.CharField(max_length=50)),
                ('marcador1', models.CharField(max_length=2)),
                ('marcador2', models.CharField(max_length=2)),
                ('fecha', models.DateField()),
                ('equipos1', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='_equipos1', to='Partidos.equipo')),
                ('equipos2', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='_equipos2', to='Partidos.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marcador1', models.CharField(max_length=2)),
                ('marcador2', models.CharField(max_length=2)),
                ('monto', models.CharField(max_length=50)),
                ('codigo_partido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Partidos.partido')),
            ],
        ),
    ]
