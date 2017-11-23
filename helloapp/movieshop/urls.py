#movieshop/urls.py

from django.conf.urls import url
from movieshop import views

urlpatterns=[
		url(r'^$', views.HomePageView.as_view()),
		]