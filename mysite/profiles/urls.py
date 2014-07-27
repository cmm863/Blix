__author__ = 'connor'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(
        r'^create_user/$',
        'profiles.views.create_user',
        name='create_user'
    ),
    url(
        r'^(?P<username>[^\.]+)/$',
        'profiles.views.view_user_profile',
        name='view_user_profile'
    )
)