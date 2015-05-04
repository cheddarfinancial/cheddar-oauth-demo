from django.conf.urls import patterns, include, url

urlpatterns = patterns('app.views',

    (r'^$', 'home'),
    (r'^account/(?P<account_id>.+)$', 'account'),

)
