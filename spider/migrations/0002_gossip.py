# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gossip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=300)),
                ('publish_date', models.DateTimeField(verbose_name=b'publishing date')),
                ('scrawl_date', models.DateTimeField(verbose_name=b'scrawling date')),
                ('status', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
