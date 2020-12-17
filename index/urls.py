from django.conf.urls import url
from . import views

app_name='index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search-tour/$', views.search_tour, name='search_tour'),
    url(r'^search-hotel/$', views.search_hotel, name='search_hotel'),
    url(r'^tours/$', views.tours, name='tours'),
    url(r'^services/$', views.services, name='services'),
    url(r'^hotels/$', views.hotels, name='hotels'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^tour-detail/(?P<slug>[-\w]+)/$', views.tour_detail, name='tour_detail'),
    url(r'^hotel-detail/(?P<slug>[-\w]+)/$', views.hotel_detail, name='hotel_detail'),

    url(r'^tours/(?P<slug>[-\w]+)/$', views.tours, name='tours_by_category'),
]