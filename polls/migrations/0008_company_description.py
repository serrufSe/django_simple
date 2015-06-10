# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150515_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
