# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('TreeFinder', '0002_auto_20150614_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='neighbourhoodName',
            field=models.CharField(default='UNSPECIFIED', max_length=200),
        ),
        migrations.AlterField(
            model_name='tree',
            name='onStreet',
            field=models.CharField(default='UNSPECIFIED', max_length=200),
        ),
        migrations.AlterField(
            model_name='treedata',
            name='file',
            field=models.FileField(default='xml data file', verbose_name='Filename', storage=django.core.files.storage.FileSystemStorage(location='/Users/M/Desktop/treeF/TreeF/uploaded_files/'), upload_to=''),
        ),
    ]
