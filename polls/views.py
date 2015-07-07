from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .forms import CompanyForm
from django.http import HttpResponseRedirect
from endless_pagination.views import AjaxListView

# Create your views here.
from polls.models import Card


def company_create(request):
	if request.method == 'POST':
		form = CompanyForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = CompanyForm()
	return render(request, 'company/create.html', {'form': form})


class CardIndex(AjaxListView):
	model = Card
	template_name = 'card/card_index.html'
	page_template = "card/card_list_page.html"

	def get_context_data(self, **kwargs):
		context = super(CardIndex, self).get_context_data(**kwargs)
		context['list'] = "card/card_list_page.html"
		return context
