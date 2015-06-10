# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20150515_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='accrual_period',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='company',
            name='updated',
            field=polls.models.UnixTimestampField(null=True),
        ),
    ]
