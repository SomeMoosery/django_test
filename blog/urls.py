from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.post_list, name='post_list') #so whenever we go to 127.0.0.1:8000, we'll be sent to the post_list view
]
