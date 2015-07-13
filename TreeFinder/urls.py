from django.conf.urls import include, url, patterns
from TreeFinder import views

urlpatterns = patterns('',
    url(r'^$', views.treefinder),
    url(r'^filter/$', views.filter, name="filter"),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    )

