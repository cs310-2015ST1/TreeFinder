# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x_coordinate', models.FloatField(default=0.0)),
                ('y_coordinate', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('species', models.CharField(max_length=200)),
                ('location', models.ForeignKey(to='TreeFinder.Location')),
            ],
        ),
        migrations.CreateModel(
            name='TreeData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(default=b'xml data file', upload_to=b'', storage=django.core.files.storage.FileSystemStorage(location=b'/Users/lkavanagh010/Desktop/L/P/TreeFinder/uploaded_files/'), verbose_name=b'Filename')),
            ],
        ),
    ]
