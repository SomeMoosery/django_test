from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.post_list, name='post_list'), #so whenever we go to 127.0.0.1:8000, we'll be sent to the post_list view
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), #looks for a d+ and stores that as variable pk, looks for pk=5 in post_list view when clicked
    url(r'^post/new/$', views.post_new, name = 'post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name = 'post_edit'),
    url(r'^drafts/$', views.post_draft_list, name = 'post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name = 'post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name = 'post_remove'),
]
