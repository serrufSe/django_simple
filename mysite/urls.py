from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls import views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'mysite.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^index', views.index),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^company/create', views.CompanyCreate.as_view(), name='company_create'),
	url(r'^company/view/(?P<pk>[0-9]+)/$', views.CompanyView.as_view(), name='company_view'),
	url(r'^card/$', views.CardIndex.as_view(), name="card_index"),
	url(r'^card/ajax_create', views.card_create_ajax, name="card_create_ajax"),
	url(r'^sale/$', views.SaleList.as_view(), name="sale_list"),
	url(r'^sale/update/(?P<pk>[0-9]+)/$', views.sale_update, name='sale_update')
)
