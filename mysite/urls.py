from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^company/create', views.company_create),
    url(r'^card', views.CardIndex.as_view()),
)
