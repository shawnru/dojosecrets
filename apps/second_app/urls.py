from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='secroot'),
    url(r'^like$', views.like, name='seclike'),
    url(r'^addsecret$', views.addsecret, name='secadd'),
    url(r'^popular$', views.popular, name='secpop'),
    url(r'^delete$', views.delete, name='secdel'),
    url(r'^logout$', views.logout, name='seclout'),
    # url(r'^session-test/$', views.session_test_1),
    # url(r'^session-test/done/$', views.session_test_2),
]
