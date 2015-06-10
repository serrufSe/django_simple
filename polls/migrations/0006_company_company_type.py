# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150515_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.PositiveSmallIntegerField(default=1, choices=[(1, b'Common'), (2, b'Communication')]),
        ),
    ]
