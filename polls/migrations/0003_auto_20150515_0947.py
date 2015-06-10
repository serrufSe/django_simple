# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='company',
            name='accrual_period',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.IntegerField(),
        ),
    ]
