# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20150515_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
