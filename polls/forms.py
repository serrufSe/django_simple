import datetime
from django.forms import ModelForm, CharField, IntegerField, HiddenInput, ChoiceField, model_to_dict, DateTimeField, \
	DateInput, SplitDateTimeWidget, DateTimeInput
from django.forms.utils import ErrorList
import time
from .models import Company, Sale, Card, Shop

class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = '__all__'


class SaleFormXML(ModelForm):

	date_pattern = "%d.%m.%Y %H:%M:%S"

	transaction_date = CharField(max_length=200)
	receipt_type = CharField(max_length=200)
	return_date = CharField(max_length=200, required=False)

	class Meta:
		model = Sale
		fields = '__all__'

	def clean_transaction_date(self):
		data = self.cleaned_data['transaction_date']
		return time.mktime(datetime.datetime.strptime(data, "%d.%m.%Y %H:%M:%S").timetuple())

	def clean_receipt_type(self):
		data = self.cleaned_data['receipt_type']
		return self.instance.get_type_key_by_name(data)

	def clean_return_date(self):
		data = self.cleaned_data['return_date']
		return time.mktime(datetime.datetime.strptime(data, "%d.%m.%Y %H:%M:%S").timetuple()) if data else None

class SaleFieldProxy:

	@staticmethod
	def get_transaction_date(value):
		return datetime.datetime.fromtimestamp(value)

	@staticmethod
	def get_return_date(value):
		return datetime.datetime.fromtimestamp(value) if value else None


class SaleFormWeb(ModelForm):

	transaction_date = DateTimeField(widget=DateTimeInput(attrs={'class':'datepicker'}))
	return_date = DateTimeField(widget=DateTimeInput(attrs={'class':'datepicker'}))

	class Meta:
		model = Sale
		fields = '__all__'

	def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
				 label_suffix=None, empty_permitted=False, instance=None):
		self.field_proxy = SaleFieldProxy
		super().__init__(self.sale_model_to_dict(instance), files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance)

	def sale_model_to_dict(self, instance):
		if instance:
			data = model_to_dict(instance)
			for k, v in data.items():
				getter_name = "_".join(("get", k))
				if hasattr(self.field_proxy, getter_name):
					data[k] = getattr(self.field_proxy, getter_name)(v)
			return data
		else:
			return None


class CardForm(ModelForm):

	def __init__(self, company, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
				 label_suffix=None, empty_permitted=False, instance=None):
		super(CardForm, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance)
		self.fields['shop'].queryset = Shop.objects.filter(company=company.id)
		self.fields['company'] = IntegerField(initial=company.id, widget=HiddenInput())

	class Meta:
		model = Card
		fields = ['number', 'shop', 'company']
