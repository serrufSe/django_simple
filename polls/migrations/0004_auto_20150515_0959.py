# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150515_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created',
            field=polls.models.UnixTimestampField(null=True, auto_created=True),
        ),
    ]
