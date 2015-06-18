# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TreeFinder', '0005_tree_civicnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='commonName',
            field=models.CharField(default='UNSPECIFIED', max_length=200),
        ),
        migrations.AddField(
            model_name='tree',
            name='genusName',
            field=models.CharField(default='UNSPECIFIED', max_length=200),
        ),
        migrations.AlterField(
            model_name='tree',
            name='species',
            field=models.CharField(default='UNSPECIFIED', max_length=200),
        ),
    ]
