# Generated by Django 4.2.13 on 2024-06-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rina_app', '0005_delete_basedimension_embarcacao_ativo_empresa_ativo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embarcacao',
            name='ativo',
            field=models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], default=1),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ativo',
            field=models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], default=1),
        ),
        migrations.AlterField(
            model_name='gerencia',
            name='ativo',
            field=models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], default=1),
        ),
        migrations.AlterField(
            model_name='status',
            name='ativo',
            field=models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], default=1),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='ativo',
            field=models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], default=1),
        ),
    ]