# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20150515_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='accrual_period',
            field=models.PositiveSmallIntegerField(default=None),
        ),
    ]
