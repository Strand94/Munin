from django.conf.urls import url
from django.contrib.auth import views as auth_views

from apps.registration import views

urlpatterns = [
    #url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    #url(r'^register$', views.register, name='register'),
    url(r'^(?P<slug>[\w.@+-]+)$', views.Profile.as_view(), name='profile'),
]