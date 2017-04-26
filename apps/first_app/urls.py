from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='logroot'),
    url(r'^register$', views.register, name='logreg'),
    url(r'^login$', views.login, name='loglog'),
    # url(r'^session-test/$', views.session_test_1),
    # url(r'^session-test/done/$', views.session_test_2),

]
