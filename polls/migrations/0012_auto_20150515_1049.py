# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20150515_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='updated',
            field=models.IntegerField(),
        ),
    ]
