# Generated by Django 5.0.3 on 2024-04-06 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('raqam', models.CharField(max_length=10)),
                ('qavat', models.PositiveSmallIntegerField()),
                ('joylar_soni', models.PositiveSmallIntegerField()),
                ('band', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Xona',
                'verbose_name_plural': 'Xonalar',
            },
        ),
        migrations.CreateModel(
            name='Joy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('raqam', models.CharField(max_length=3)),
                ('xona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomsApp.xona')),
            ],
            options={
                'verbose_name': 'Joy',
                'verbose_name_plural': 'Joylar',
            },
        ),
    ]
