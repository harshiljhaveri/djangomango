from django.urls import path, include 
from marketing.views import sdml
from django.conf.urls import url

urlpatterns = [
	url('sendmail/', sdml, name='sendmail'),
	]
