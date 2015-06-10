# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_company_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created',
            field=polls.models.UnixTimestampField(null=True),
        ),
    ]
