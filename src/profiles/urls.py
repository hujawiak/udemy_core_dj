# coding=utf-8
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
from dashboard.views import DashboardTemplateView, MyView, BookDetailView, BookListView, BookCreateView, \
    BookUpdateView, BookDeleteView


app_name = 'profiles'
urlpatterns = [
    url(r'^$', views.home, name='home'),
url(r'^about/$', DashboardTemplateView.as_view(), name='about'),

url(r'^book/$', BookListView.as_view(), name='book_list'),
url(r'^book/create/$', BookCreateView.as_view(), name='book_create'),
url(r'^book/(?P<slug>[-\w]+)/update/$', BookUpdateView.as_view(), name='book_update'),
url(r'^book/(?P<slug>[-\w]+)/delete/$', BookDeleteView.as_view(), name='book_delete'),
url(r'^book/(?P<slug>[-\w]+)/$', BookDetailView.as_view(), name='book_detail'),

#url(r'^about/$', views.about, name='about'),
url(r'^base_dupa/$', MyView.as_view(), name='base_dupa'),
url(r'^profile/$', views.user_profile, name='profile'),
url(r'^filters/$', views.filters, name='filters'),

]