from django.conf.urls import include, url, patterns
from TreeFinder import views

urlpatterns = patterns('',
    url(r'^$', views.treefinder),
        url(r'^filter/$', views.filter, name="filter"),
    )

