# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('company_type', models.CharField(default=b'common', max_length=1, choices=[(b'common', b'Common'), (b'communication', b'Communication')])),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created', models.IntegerField(max_length=11)),
                ('accrual_period', models.IntegerField(max_length=11)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
