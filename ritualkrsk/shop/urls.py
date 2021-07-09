from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home_page, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    url(r'^(page)/(\d+)/$', views.home_page, name='home_pages'),
]