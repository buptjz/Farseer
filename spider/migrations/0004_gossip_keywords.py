# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0003_auto_20150115_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='gossip',
            name='keywords',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
