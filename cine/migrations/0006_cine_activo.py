# Generated by Django 4.1.2 on 2022-11-17 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0005_alter_usuario_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='cine',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
