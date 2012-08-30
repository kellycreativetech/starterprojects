from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="homepage"),
)

urlpatterns += staticfiles_urlpatterns()
