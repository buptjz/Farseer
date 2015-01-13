# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('content', models.TextField()),
                ('scrawl_date', models.DateTimeField(verbose_name=b'date scrawling')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
