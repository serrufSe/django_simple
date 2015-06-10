# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
import xml.etree.ElementTree as ET
import os
import polls
from polls.sale_xml_creator import SaleXMLCreator
from polls.sale_source_data_generator import SaleXMLSourceDataGenerator
from polls.sale_xml_parser import SaleXMLParser


class Command(BaseCommand):

	def handle(self, *args, **options):

		local_file = os.path.join(os.path.dirname(os.path.realpath(polls.__file__)), 'upload', 'test.xml')
		sale_xml_creator = SaleXMLCreator(SaleXMLSourceDataGenerator(SaleXMLParser(ET.parse(local_file))))
		sale_xml_creator.start_create()

