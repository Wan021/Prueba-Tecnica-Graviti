# Generated by Django 3.1.3 on 2023-02-01 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nacionalidades',
            fields=[
                ('codigo', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nacionalidad_masculino', models.CharField(max_length=50)),
                ('nacionalidad_femenino', models.CharField(max_length=50)),
            ],
        ),
    ]
