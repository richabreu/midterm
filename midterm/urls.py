#from django.conf.urls import patterns, url
from django.conf.urls import url
from midterm import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^addcart/(?P<user_id>\w+)/(?P<entry_id>\w+)/$', views.addcart, name='addcart'),
    url(r'^entry/(?P<entry_id>\w+)/$', views.entry, name='entry'),
    url(r'^viewcart/(?P<user_id>\w+)/', views.viewcart, name='viewcart'),
]
