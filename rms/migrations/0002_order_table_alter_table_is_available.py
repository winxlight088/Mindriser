# Generated by Django 5.1.4 on 2024-12-26 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rms.table'),
        ),
        migrations.AlterField(
            model_name='table',
            name='is_available',
            field=models.CharField(choices=[('Available', 'Seat Available'), ('Unavailable', 'Seat Unavailable')], default='Unavailable', max_length=30),
        ),
    ]
