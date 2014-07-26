__author__ = 'connor'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(
        r'^view/(?P<slug>[^\.]+).html',
        'blog.views.view_post',
        name='view_blog_post'
    ),
    url(
        r'^category/(?P<slug>[^\.]+).html',
        'blog.views.view_category',
        name='view_blog_category'
    ),
    url(
        r'^create_category/$',
        'blog.views.create_category'
    ),
    url(
        r'^create_post/$',
        'blog.views.create_post'
    )
)