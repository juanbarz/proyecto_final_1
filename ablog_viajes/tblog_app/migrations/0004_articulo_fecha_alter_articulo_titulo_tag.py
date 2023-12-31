# Generated by Django 4.2.2 on 2023-06-28 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tblog_app', '0003_rename_publicacion_articulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo_tag',
            field=models.CharField(max_length=255),
        ),
    ]
