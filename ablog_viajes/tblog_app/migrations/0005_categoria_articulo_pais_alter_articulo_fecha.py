# Generated by Django 4.2.2 on 2023-06-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tblog_app', '0004_articulo_fecha_alter_articulo_titulo_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(default='N/A', max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='pais',
            field=models.CharField(default='N/A', max_length=30),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]