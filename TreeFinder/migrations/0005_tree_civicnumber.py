# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TreeFinder', '0004_filterrequestobject'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='civicNumber',
            field=models.IntegerField(default=0),
        ),
    ]
