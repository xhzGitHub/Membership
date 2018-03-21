from django.conf.urls import url
from . import views


urlpatterns = [
    url('^main/$',views.main),
    url('^regist/$',views.regist),
    url(r'^checkuserid/$', views.checkuserid),
    url(r'^login/$', views.login),
    url(r'^quit/$', views.quit),
]
