# -*- coding: utf-8 -*-

from .forms import SaleFormXML


class SaleXMLCreator(object):

	@staticmethod
	def create(xml_data_generator):
		for sale_data in xml_data_generator.get_sale_data():
			form = SaleFormXML(sale_data)
			if form.is_valid():
				form.save()
			else:
				print(form.errors)
