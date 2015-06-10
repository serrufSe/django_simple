# -*- coding: utf-8 -*-

from .models import Sale
import xml.etree.ElementTree as ET
from .sale_source_data_generator import SaleXMLSourceDataGenerator
from .forms import SaleForm

class SaleXMLCreator(object):

	def __init__(self, sale_generator):
		self.sale_generator = sale_generator

	def start_create(self):
		count_sale_create = 0
		count_sale_error = 0
		for sale_data in self.sale_generator.get_sale_data():
			form = SaleForm(sale_data)
			if form.is_valid():
				form.save()
				count_sale_create += 1
			else:
				count_sale_error += 1
