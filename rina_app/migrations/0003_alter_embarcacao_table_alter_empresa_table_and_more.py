# Generated by Django 4.2.13 on 2024-06-07 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rina_app', '0002_alter_recursos_prazo_nuvem'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='embarcacao',
            table='qua_embarcacao',
        ),
        migrations.AlterModelTable(
            name='empresa',
            table='qua_empresa',
        ),
        migrations.AlterModelTable(
            name='gerencia',
            table='qua_gerencia',
        ),
        migrations.AlterModelTable(
            name='recursos',
            table='qua_recurso',
        ),
        migrations.AlterModelTable(
            name='status',
            table='qua_status_recurso',
        ),
        migrations.AlterModelTable(
            name='tipo',
            table='qua_tipo',
        ),
    ]
