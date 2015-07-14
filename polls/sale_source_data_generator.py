# -*- coding: utf-8 -*-


class SaleXMLSourceDataGenerator():

	def __init__(self, sale_xml_parser, field_converter):
		self.sale_xml_parser = sale_xml_parser
		self.field_converter = field_converter

	def get_sale_data(self):
		for sale_xml in self.sale_xml_parser.get_sale_xml():

			yield self.field_converter.get_data(sale_xml)




