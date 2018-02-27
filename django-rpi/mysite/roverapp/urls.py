from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('commandforward', views.cforward, name='forward'),
    url('commandbackward', views.cbackward, name='backward'),
    url('commandleft', views.cleft, name='left'),
    url('commandright', views.cright, name='right'),
    url('commandidle', views.cidle, name='idle'),
    url('commandup', views.cup, name='up'),
    url('commanddown', views.cdown, name='down')

]