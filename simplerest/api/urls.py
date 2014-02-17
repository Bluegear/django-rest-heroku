from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'simplerest.api.views.home'),
    url(r'^list/', 'simplerest.api.views.api_list'),
)

