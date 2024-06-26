# Generated by Django 5.0.3 on 2024-04-06 08:41

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
        ('studentsApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='fakultet',
        ),
        migrations.RemoveField(
            model_name='student',
            name='haqdor',
        ),
        migrations.RemoveField(
            model_name='student',
            name='kurs',
        ),
        migrations.RemoveField(
            model_name='student',
            name='qarzdor',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tutor',
        ),
        migrations.AddField(
            model_name='student',
            name='balans',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Guruh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=255)),
                ('kurs', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('fakultet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.fakultet')),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Guruh',
                'verbose_name_plural': 'Guruhlar',
            },
        ),
    ]
