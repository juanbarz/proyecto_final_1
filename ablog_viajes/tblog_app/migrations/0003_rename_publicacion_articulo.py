# Generated by Django 4.2.2 on 2023-06-27 23:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tblog_app', '0002_publicacion_titulo_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publicacion',
            new_name='Articulo',
        ),
    ]
