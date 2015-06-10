# -*- coding: utf-8 -*-
from .models import Sale

class SaleXMLSourceDataGenerator(object):

	def __init__(self, sale_xml_parser):
		self.sale_xml_parser = sale_xml_parser

	def get_sale_data(self):
		for sale_xml in self.sale_xml_parser.get_sale_xml():
			yield sale_xml

