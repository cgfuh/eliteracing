# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_adjust_coursescreenshot_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srvcrosscourse',
            name='gravity',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='srvrallycourse',
            name='gravity',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='srvrallycourse',
            name='planet_type',
            field=models.CharField(choices=[(b'rock', b'Rock'), (b'ice', b'Ice'), (b'lava', b'Lava'), (b'metallic', b'Metallic'), (b'water', b'Water'), (b'earth-like', b'Earth-Like'), (b'ammonia', b'Ammonia'), (b'gas', b'Gas')], db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='stadiumcourse',
            name='gravity',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='surfacecourse',
            name='gravity',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='zerogravitycourse',
            name='number_of_rings',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]
