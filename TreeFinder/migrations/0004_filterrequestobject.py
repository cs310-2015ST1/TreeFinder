# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TreeFinder', '0003_auto_20150614_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterRequestObject',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('CivicNumber', models.IntegerField(default=0)),
                ('OnStreet', models.CharField(max_length=200, default='UNSPECIFIED')),
                ('HeightRangeID', models.IntegerField(default=0)),
                ('Diameter', models.IntegerField(default=0)),
                ('GenusName', models.CharField(max_length=200, default='UNSPECIFIED')),
                ('SpeciesName', models.CharField(max_length=200, default='UNSPECIFIED')),
                ('CommonName', models.CharField(max_length=200, default='UNSPECIFIED')),
            ],
        ),
    ]
