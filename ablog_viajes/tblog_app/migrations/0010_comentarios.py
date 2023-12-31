# Generated by Django 4.2.2 on 2023-07-01 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tblog_app', '0009_perfil_facebook_perfil_imagen_perfil_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=155)),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='tblog_app.articulo')),
            ],
        ),
    ]
