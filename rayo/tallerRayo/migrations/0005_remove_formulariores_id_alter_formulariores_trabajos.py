# Generated by Django 4.2.2 on 2023-07-07 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallerRayo', '0004_formulariores_atencion_categoria_atencion_materiales_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulariores',
            name='id',
        ),
        migrations.AlterField(
            model_name='formulariores',
            name='trabajos',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
