from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'firstapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^login/$', 'loginsys.views.login'),
                       url(r'^logout/$', 'loginsys.views.logout'),
                       url(r'^register/$', 'loginsys.views.register'),

                       )
