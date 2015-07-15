import datetime
from django.forms import ModelForm, CharField, IntegerField, HiddenInput, ChoiceField
from django.forms.utils import ErrorList
import time
from .models import Company, Sale, Card, Shop

class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = '__all__'


class SaleForm(ModelForm):
	class Meta:
		model = Sale
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


class CardForm(ModelForm):

	def __init__(self, company, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
				 label_suffix=None, empty_permitted=False, instance=None):
		super(CardForm, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance)
		self.fields['shop'].queryset = Shop.objects.filter(company=company.id)
		self.fields['company'] = IntegerField(initial=company.id, widget=HiddenInput())

	class Meta:
		model = Card
		fields = ['number', 'shop', 'company']
