# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20150515_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='updated',
            field=models.IntegerField(null=True),
        ),
    ]
