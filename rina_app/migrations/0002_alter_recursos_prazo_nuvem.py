# Generated by Django 4.2.13 on 2024-06-01 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rina_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recursos',
            name='prazo_nuvem',
            field=models.IntegerField(),
        ),
    ]
