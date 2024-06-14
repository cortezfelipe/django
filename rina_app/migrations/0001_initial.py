# Generated by Django 4.2.13 on 2024-06-01 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Embarcacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('embarcacao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('empresa', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gerencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gerencia', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recursos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prazo_nuvem', models.IntegerField(max_length=11)),
                ('embarcacao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rina_app.embarcacao')),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rina_app.empresa')),
                ('gerencia_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rina_app.gerencia')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rina_app.status')),
                ('tipo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rina_app.tipo')),
            ],
        ),
    ]