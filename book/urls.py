from django.conf.urls import url
from . import views

app_name='book'
urlpatterns = [
   url(r'^book-tour/(?P<slug>[-\w]+)/$', views.book_tour, name='book_tour'),
   url(r'^book-room/(?P<slug>[-\w]+)/$', views.book_room, name='book_room'),
]