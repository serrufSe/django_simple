# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150515_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='accrual_period',
        ),
        migrations.RemoveField(
            model_name='company',
            name='address',
        ),
        migrations.RemoveField(
            model_name='company',
            name='company_type',
        ),
        migrations.RemoveField(
            model_name='company',
            name='created',
        ),
        migrations.RemoveField(
            model_name='company',
            name='description',
        ),
        migrations.RemoveField(
            model_name='company',
            name='email',
        ),
    ]
