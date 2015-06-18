# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TreeFinder', '0006_auto_20150617_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filterrequestobject',
            name='Diameter',
        ),
    ]
