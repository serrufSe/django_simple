# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model
from polls.models import Sale, Card, Seller, Shop


class XMLAttributeToSaleFieldConverter:

	def __init__(self, sale_fields, company_id):
		self.sale_fields = sale_fields
		self.sale_data = {}
		self.attribute_map = {
			Sale._meta.get_field('article').name: SaleField('Артикул'),
			Sale._meta.get_field('title').name: SaleField('Наименование'),
			Sale._meta.get_field('count').name: SaleField('Количество'),
			Sale._meta.get_field('price').name: SaleField('Сумма'),
			Sale._meta.get_field('discount').name: SaleField('СуммаСкидки'),
			Sale._meta.get_field('discount_type').name: SaleField('ТипАкции'),
			Sale._meta.get_field('discount_name').name: SaleField('НаименованиеАкции'),
			Sale._meta.get_field('shop_id').name: ShopSaleField(shop_name_field='ИмяМагазина', shop_code_field='КодМагазина', company_id= company_id),
			Sale._meta.get_field('transaction_date').name: SaleField('ДатаВремяТранзакции'),
			Sale._meta.get_field('receipt_number').name: SaleField('НомерЧека'),
			Sale._meta.get_field('receipt_type').name: SaleField('ВидЧека'),
			Sale._meta.get_field('receipt_number_return').name: SaleField('НомерЧекаВозврата'),
			Sale._meta.get_field('return_date').name: SaleField('ДатаЧекаВозврата'),
			Sale._meta.get_field('card_id').name: CardField('НомерКарты', company_id= company_id),
			Sale._meta.get_field('seller_id').name: SellerField('Продавец', company_id= company_id),
	}

	def get_data(self, xml_data):

		for field in self.sale_fields:
			sale_field = self.attribute_map[field]
			self.sale_data[field] = sale_field.resolve_value(xml_data)
		return self.sale_data


class SimpleXMLField:

	def __init__(self, xml_key):
		self.xml_key = xml_key

class SaleField(SimpleXMLField):

	def resolve_value(self, xml_data):
		return xml_data[self.xml_key]


class DependOnCompanyForeignSaleField(SaleField):

	def __init__(self, xml_key, company_id):
		super(DependOnCompanyForeignSaleField, self).__init__(xml_key)
		self.company_id = company_id

class ForeignFieldMixin:
	model = Model

	def get_instance_pk(self, kwargs):
		try:
			instance = self.model.objects.get(**kwargs)
			return instance.id
		except ObjectDoesNotExist:
			new_instance = self.model(**kwargs)
			new_instance.full_clean()
			new_instance.save()
			return new_instance.id

class CardField(DependOnCompanyForeignSaleField, ForeignFieldMixin):
	model = Card

	def resolve_value(self, xml_data):
		card_number = super(CardField, self).resolve_value(xml_data)
		if (card_number):
			kwargs = {'number': card_number, 'company_id': self.company_id}
			return self.get_instance_pk(kwargs)
		else:
			return None


class SellerField(DependOnCompanyForeignSaleField, ForeignFieldMixin):
	model = Seller

	def resolve_value(self, xml_data):
		seller_info = super(SellerField, self).resolve_value(xml_data).split(" ")

		if len(seller_info) == 3:
			second_name, fist_name, last_name = super(SellerField, self).resolve_value(xml_data).split(" ")
			kwargs = {'name': fist_name, 'second_name': second_name, 'last_name': last_name, 'company_id': self.company_id}
		else:
			second_name, fist_name = super(SellerField, self).resolve_value(xml_data).split(" ")
			kwargs = {'name': fist_name, 'second_name': second_name, 'company_id': self.company_id}

		return self.get_instance_pk(kwargs)


class ShopSaleField(ForeignFieldMixin):
	model = Shop

	def __init__(self, shop_name_field, shop_code_field, company_id):
		self.shop_name = shop_name_field
		self.shop_code = shop_code_field
		self.company_id = company_id

	def resolve_value(self, xml_data):
		kwargs = {'code': self.shop_code, 'name': self.shop_name, 'company_id': self.company_id}

		return self.get_instance_pk(kwargs)