# Generated by Django 4.1.2 on 2022-10-26 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0002_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='token',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
