# -*- coding: utf-8 -*-

class SaleXMLParser(object):

	root_tag = u'Товары'

	def __init__(self, xml_parse):
		self.xml_parser = xml_parse

	def get_sale_xml(self):
		root = self.xml_parser.getroot()

		for sale in root.findall(self.root_tag):
			sale_info = {}

			for attr in sale.attrib:
				sale_info[attr] = sale.get(attr)

			yield sale_info
