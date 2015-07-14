# -*- coding: utf-8 -*-

from .models import Sale
import xml.etree.ElementTree as ET
from .sale_source_data_generator import SaleXMLSourceDataGenerator
from .forms import SaleForm

class SaleXMLCreator(object):

	@staticmethod
	def create(xml_data_generator):
		for sale_data in xml_data_generator.get_sale_data():
			form = SaleForm(sale_data)
			if form.is_valid():
				form.save()
			else:
				print(form.errors)
