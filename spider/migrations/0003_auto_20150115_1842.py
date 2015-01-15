# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0002_gossip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gossip',
            name='publish_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gossip',
            name='scrawl_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gossip',
            name='status',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
