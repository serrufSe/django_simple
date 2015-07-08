# -*- coding: utf-8 -*-

from datetime import datetime
from time import strftime
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text


class UnixTimestampField(models.DateTimeField):
	"""UnixTimestampField: creates a DateTimeField that is represented on the
	database as a TIMESTAMP field rather than the usual DATETIME field.
	"""

	def __init__(self, null=False, blank=False, **kwargs):
		super(UnixTimestampField, self).__init__(**kwargs)
		# default for TIMESTAMP is NOT NULL unlike most fields, so we have to
		# cheat a little:
		self.blank, self.isnull = blank, null
		self.null = True # To prevent the framework from shoving in "not null".

	def db_type(self, connection):
		typ = ['TIMESTAMP']
		# See above!
		if self.isnull:
			typ += ['NULL']
		if self.auto_created:
			typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
		return ' '.join(typ)

	def to_python(self, value):
		if isinstance(value, int):
			return datetime.fromtimestamp(value)
		else:
			return models.DateTimeField.to_python(self, value)

	def get_db_prep_value(self, value, connection, prepared=False):
		if value == None:
			return None
			# Use '%Y%m%d%H%M%S' for MySQL < 4.1
		return strftime('%Y-%m-%d %H:%M:%S', value.timetuple())


class Company(models.Model):

	TYPE_COMMON = 1
	TYPE_COMMUNICATION = 2
	COMPANY_TYPE = (
		(TYPE_COMMON, 'Common'),
		(TYPE_COMMUNICATION, 'Communication')
	)

	name = models.CharField(max_length=200)
	company_type = models.PositiveSmallIntegerField(choices=COMPANY_TYPE, default=TYPE_COMMON)
	email = models.EmailField(default=None)
	address = models.CharField(max_length=200, default=None)
	description = models.TextField(blank=True)
	created = models.IntegerField()
	accrual_period = models.PositiveSmallIntegerField(default=None)
	updated = models.IntegerField(null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "/company/view/%i/" % self.id


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return  self.choice_text

class Shop(models.Model):
	code = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	company = models.ForeignKey(Company)

	def __str__(self):
		return self.name


class Card(models.Model):
	number = models.CharField(max_length=200)
	company = models.ForeignKey(Company, null=True)
	shop = models.ForeignKey(Shop)


class Seller(models.Model):
	name = models.CharField(max_length=200)
	second_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)


class Sale(models.Model):

	RECEIPT_TYPE_SALE = 1
	RECEIPT_TYPE_RETURN = 2
	RECEIPT_TYPE = (
		(RECEIPT_TYPE_SALE, u'Продажа'),
		(RECEIPT_TYPE_RETURN, u'Возврат')
	)

	article = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	count = models.PositiveIntegerField()
	price = models.PositiveIntegerField()
	discount = models.PositiveIntegerField(blank=True, null=True)
	discount_type = models.CharField(max_length=200, blank=True, null=True)
	discount_name = models.CharField(max_length=200, blank=True, null=True)
	shop = models.ForeignKey(Shop)
	transaction_date = models.PositiveIntegerField()
	receipt_number = models.CharField(max_length=200)
	receipt_type = models.PositiveSmallIntegerField(RECEIPT_TYPE)
	receipt_number_return = models.CharField(max_length=200, blank=True, null=True)
	return_date = models.PositiveIntegerField(blank=True, null=True)
	card = models.ForeignKey(Card)
	seller = models.ForeignKey(Seller)

