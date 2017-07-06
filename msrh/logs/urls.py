from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^test/', views.test, name='test'),
    url(r'^make/$', views.maketraining),
    url(r'^show/', views.shows),
    url(r'^addt/$', views.make, name='addtrain'),
]