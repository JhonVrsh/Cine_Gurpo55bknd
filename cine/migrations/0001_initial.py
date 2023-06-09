# Generated by Django 4.1.2 on 2022-10-15 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.CharField(max_length=5)),
                ('genero', models.CharField(max_length=20)),
                ('director', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numeroAcientos', models.IntegerField()),
                ('cine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.cine')),
            ],
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('valor', models.IntegerField()),
                ('hora', models.DateTimeField()),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.pelicula')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asientos', models.CharField(max_length=50)),
                ('valor', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.cliente')),
                ('funcion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.funcion')),
            ],
        ),
    ]
