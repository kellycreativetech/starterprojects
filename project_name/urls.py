from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from servee import frontendadmin

admin.autodiscover()
frontendadmin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^servee/", include(frontendadmin.site.urls)),

    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="homepage"),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
        'template_name': 'accounts/login.html'}, name="acct_login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/'}, name="acct_logout"),

)

urlpatterns += staticfiles_urlpatterns()
