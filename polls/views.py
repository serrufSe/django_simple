from django.shortcuts import render
from .forms import CompanyForm
from django.http import HttpResponseRedirect

# Create your views here.

def company_create(request):
	if request.method == 'POST':
		form = CompanyForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = CompanyForm()
	return render(request, 'company/create.html', {'form' : form})
