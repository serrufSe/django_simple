from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic import View, CreateView, DetailView, ListView
from .forms import CompanyForm, CardForm, SaleFormWeb
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from endless_pagination.views import AjaxListView
from django.forms.models import modelform_factory

# Create your views here.
from polls.models import Card, Company, Sale


def index(request):
	return HttpResponse('Index')

def company_create(request):
	form = CompanyForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/')
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

def sale_update(request, pk):
	instance = get_object_or_404(Sale, id=pk)
	form = SaleFormWeb(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request, 'sale/update.html', {'form': form})


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


class SaleList(ListView):
	model = Sale
	template_name = 'sale/list.html'


