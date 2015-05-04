from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'app.views.home'),
    url('oauth/', include('social.apps.django_app.urls', namespace='social'))
)
