# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
import xml.etree.ElementTree as ET
import os
from django.db.models import AutoField
import polls
from polls.models import Sale
from polls.sale_xml_creator import SaleXMLCreator
from polls.sale_source_data_generator import SaleXMLSourceDataGenerator
from polls.xml_mapping import XMLAttributeToSaleFieldConverter
from polls.sale_xml_parser import SaleXMLParser


class Command(BaseCommand):

	def handle(self, *args, **options):

		company_id = 1
		local_file = os.path.join(os.path.dirname(os.path.realpath(polls.__file__)), 'upload', 'test.xml')
		SaleXMLCreator.create(
			SaleXMLSourceDataGenerator(
				SaleXMLParser(
					ET.parse(local_file)
				),
				XMLAttributeToSaleFieldConverter(
					[f.name for f in Sale._meta.fields if not isinstance(f, AutoField)],
					company_id
				),
			)
		)

