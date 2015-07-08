from django.forms import ModelForm, CharField, ModelChoiceField, IntegerField, HiddenInput
from django.forms.utils import ErrorList
from .models import Company, Sale, Card, Shop


class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = '__all__'


class SaleForm(ModelForm):
	class Meta:
		model = Sale
		fields = '__all__'

class CardForm(ModelForm):

	def __init__(self, company, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
				 label_suffix=None, empty_permitted=False, instance=None):
		super(CardForm, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance)
		self.fields['shop'].queryset = Shop.objects.filter(company=company.id)
		self.fields['company'] = IntegerField(initial=company.id, widget=HiddenInput())

	class Meta:
		model = Card
		fields = ['number', 'shop', 'company']
