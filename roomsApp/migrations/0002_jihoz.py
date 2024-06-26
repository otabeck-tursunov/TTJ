# Generated by Django 5.0.3 on 2024-04-06 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jihoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=255)),
                ('soni', models.PositiveSmallIntegerField()),
                ('izoh', models.TextField(blank=True)),
                ('xona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomsApp.xona')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
