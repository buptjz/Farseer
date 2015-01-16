# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0004_gossip_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='gossip',
            name='source_url',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
