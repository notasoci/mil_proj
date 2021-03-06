# Generated by Django 2.1.4 on 2018-12-23 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Miliciano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(verbose_name='Cédula: ')),
                ('apellidos', models.CharField(max_length=30, verbose_name='Apellidos: ')),
                ('nombres', models.CharField(max_length=30, verbose_name='Nombres: ')),
                ('rango', models.CharField(max_length=20, verbose_name='Rango: ')),
                ('fecha_nacimiento', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Nacimiento: ')),
                ('fecha_ingreso', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Ingreso: ')),
                ('cedula_pareja', models.IntegerField(verbose_name='Cédula de pareja: ')),
                ('apellidos_pareja', models.CharField(max_length=30, verbose_name='Apellidos de su pareja: ')),
                ('nombres_pareja', models.CharField(max_length=30, verbose_name='Nombres de su pareja: ')),
                ('miliciana_pareja', models.BooleanField(verbose_name='Pareja milician@: ')),
                ('uniforme_zamorano', models.BooleanField(default=False, verbose_name='Uniforme Zamorano: ')),
                ('uniforme_miliciano', models.BooleanField(default=False, verbose_name='Uniforme Kaki: ')),
                ('uniforme_camuflaje', models.BooleanField(default=False, verbose_name='Uniforme camuflado: ')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo: ')),
                ('observaciones', models.CharField(max_length=200, verbose_name='Observaciones: ')),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('registrador', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddIndex(
            model_name='miliciano',
            index=models.Index(fields=['cedula', 'apellidos', 'cedula_pareja', 'apellidos_pareja'], name='milicia_mil_cedula_bba8bb_idx'),
        ),
        migrations.AddIndex(
            model_name='miliciano',
            index=models.Index(fields=['cedula'], name='cedula_idx'),
        ),
        migrations.AddIndex(
            model_name='miliciano',
            index=models.Index(fields=['apellidos'], name='apellidos_idx'),
        ),
        migrations.AddIndex(
            model_name='miliciano',
            index=models.Index(fields=['cedula_pareja'], name='cedula_pareja_idx'),
        ),
    ]
