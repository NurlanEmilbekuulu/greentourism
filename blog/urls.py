from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^(?P<slug>[-\w]+)/$', views.article_list, name='article_list_by_category'),
    url(r'^article/(?P<slug>[-\w]+)/$', views.article_detail, name='article_detail'),
]