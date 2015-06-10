# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_company_company_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
