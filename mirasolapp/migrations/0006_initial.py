# Generated by Django 5.0.6 on 2024-06-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mirasolapp', '0005_delete_servicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='items/')),
                ('titulo', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telefono', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=50)),
            ],
        ),
    ]
