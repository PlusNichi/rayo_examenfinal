# Generated by Django 4.2.2 on 2023-07-07 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallerRayo', '0003_alter_formulariocontacto_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='formularioRes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trabajos', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=50)),
                ('tipoAtencion', models.CharField(max_length=50)),
                ('diasHabiles', models.CharField(max_length=30)),
                ('justificacion', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='atencion',
            name='categoria',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='atencion',
            name='materiales',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='atencion',
            name='verify',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]