from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Django admin urls
    url(r'^admin/', include(admin.site.urls)),

    # Django index
    (r'^$', 'blog.views.index'),

    # Django blog app urls
    url(r'^blog/', include('blog.urls')),

    # Django profiles urls (user and group)
    url(r'^profile/', include('profiles.urls'))

)
