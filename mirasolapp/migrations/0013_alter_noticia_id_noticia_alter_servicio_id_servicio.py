# Generated by Django 5.0.6 on 2024-07-10 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirasolapp', '0012_alter_noticia_id_noticia_alter_servicio_id_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='id_noticia',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='id_servicio',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
