# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_add_indexes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srvrallycourse',
            name='planet_type',
            field=models.CharField(choices=[(b'rock', b'Rock'), (b'ice', b'Ice'), (b'lava', b'Lava'), (b'metallic', b'Metallic'), (b'water', b'Water'), (b'earth-like', b'Earth-Like'), (b'ammonia', b'Ammonia'), (b'gas', b'Gas')], db_index=True, default=b'rock', max_length=32),
        ),
    ]
