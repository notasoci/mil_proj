# Generated by Django 2.1.4 on 2018-12-24 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milicia', '0003_auto_20181223_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miliciano',
            name='cedula',
            field=models.CharField(max_length=10, verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='miliciano',
            name='cedula_pareja',
            field=models.CharField(max_length=10, verbose_name='Cédula de pareja'),
        ),
    ]
