# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TreeFinder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='location',
        ),
        migrations.AddField(
            model_name='tree',
            name='cell',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tree',
            name='heightRangeID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tree',
            name='neighbourhoodName',
            field=models.CharField(default=b'UNSPECIFIED', max_length=200),
        ),
        migrations.AddField(
            model_name='tree',
            name='onStreet',
            field=models.CharField(default=b'UNSPECIFIED', max_length=200),
        ),
        migrations.AddField(
            model_name='tree',
            name='onStreetBlock',
            field=models.IntegerField(default=0),
        ),
    ]
