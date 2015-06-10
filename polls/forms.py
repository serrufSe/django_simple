from django.forms import ModelForm, CharField
from .models import Company, Sale


class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = '__all__'


class SaleForm(ModelForm):
	class Meta:
		model = Sale
		fields = '__all__'
