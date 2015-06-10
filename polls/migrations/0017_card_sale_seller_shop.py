# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20150515_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('count', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(null=True, blank=True)),
                ('discount_type', models.CharField(max_length=200, null=True, blank=True)),
                ('discount_name', models.CharField(max_length=200, null=True, blank=True)),
                ('transaction_date', models.PositiveIntegerField()),
                ('receipt_number', models.CharField(max_length=200)),
                ('receipt_type', models.PositiveSmallIntegerField(verbose_name=((1, '\u041f\u0440\u043e\u0434\u0430\u0436\u0430'), (2, '\u0412\u043e\u0437\u0432\u0440\u0430\u0442')))),
                ('receipt_number_return', models.CharField(max_length=200, null=True, blank=True)),
                ('return_date', models.PositiveIntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
