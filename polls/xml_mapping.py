from django.core.exceptions import ObjectDoesNotExist
from polls.models import Sale, Card, Seller, Shop


class XMLAttributeToSaleFieldConverter:

	def __init__(self, sale_fields, company_id):
		self.sale_fields = sale_fields
		self.sale_data = []
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
			field = self.attribute_map[field]
			self.sale_data[field] = field.resolve_value(xml_data)
		return self.sale_data


class Field:

	def resolve_value(self, xml_data):
		pass


class SimpleXMLField(Field):

	def __init__(self, xml_key):
		self.xml_key = xml_key

class SaleField(SimpleXMLField):

	def resolve_value(self, xml_data):
		return xml_data[self.xml_key]


class DependOnCompanyForeignSaleField(SimpleXMLField):

	def __init__(self, xml_key, company_id):
		super().__init__(xml_key)
		self.company_id = company_id


class CardField(DependOnCompanyForeignSaleField):

	def resolve_value(self, xml_data):
		card_number = super().resolve_value(xml_data)
		kwargs = {'number': card_number, 'company': self.company_id}
		try:
			card_model = Card.objects.get(kwargs)
		except ObjectDoesNotExist:
			card_model = Card(kwargs)
			card_model.save()
		finally:
			return card_model.id


class SellerField(DependOnCompanyForeignSaleField):

	def resolve_value(self, xml_data):
		seller_info = super().resolve_value(xml_data).split(" ")

		if len(seller_info) == 3:
			second_name, fist_name, last_name = super().resolve_value(xml_data).split(" ")
			kwargs = {'name': fist_name, 'second_name': second_name, 'last_name': last_name, 'company': self.company_id}
		else:
			second_name, fist_name = super().resolve_value(xml_data).split(" ")
			kwargs = {'name': fist_name, 'second_name': second_name, 'company': self.company_id}

		try:
			seller = Seller.objects.get(kwargs)
		except ObjectDoesNotExist:
			seller = Seller(kwargs)
			seller.save()
		finally:
			return seller.id


class ShopSaleField(Field):

	def __init__(self, shop_name_field, shop_code_field, company_id):
		self.shop_name = shop_name_field
		self.shop_code = shop_code_field
		self.company_id = company_id

	def resolve_value(self, xml_data):
		kwargs = {'code': self.shop_code, 'name': self.shop_name, 'company': self.company_id}
		try:
			shop = Shop.objects.get(kwargs)
		except ObjectDoesNotExist:
			shop = Shop(kwargs)
			shop.save()
		finally:
			return shop.id