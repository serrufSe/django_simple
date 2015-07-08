from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import View, CreateView, DetailView
from .forms import CompanyForm, CardForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from endless_pagination.views import AjaxListView
from django.forms.models import modelform_factory

# Create your views here.
from polls.models import Card, Company


def index(request):
	return HttpResponse('Index')

def company_create(request):
	if request.method == 'POST':
		form = CompanyForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = CompanyForm()
	return render(request, 'company/create.html', {'form': form})

def card_create_ajax(request):
	if request.method == 'POST' and request.is_ajax():
		card_form = modelform_factory(model=Card, fields='__all__')
		form = card_form(request.POST)
		if form.is_valid():
			card = form.save()
			return JsonResponse({'result': 'success',  'data': card.number})
		else:
			return JsonResponse({'result': 'error', 'data': form.errors})
	raise FileNotFoundError()


class CardIndex(AjaxListView):
	model = Card
	template_name = 'card/card_index.html'
	page_template = "card/card_list_page.html"

	def get_context_data(self, **kwargs):
		context = super(CardIndex, self).get_context_data(**kwargs)
		context['list'] = "card/card_list_page.html"
		return context

class CompanyCreate(CreateView):
	model = Company
	fields = '__all__'
	template_name = 'company/create.html'

class CompanyView(DetailView):
	model = Company
	template_name = 'company/view.html'

	def get_context_data(self, **kwargs):
		context = super(CompanyView, self).get_context_data(**kwargs)
		context['card_form'] = CardForm(company=self.object)
		return context
