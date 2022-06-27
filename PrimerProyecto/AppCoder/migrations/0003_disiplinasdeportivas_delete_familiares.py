# Generated by Django 4.0.5 on 2022-06-26 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alter_familiares_anio_de_nacimiento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisiplinasDeportivas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
        ),
        migrations.DeleteModel(
            name='Familiares',
        ),
    ]
