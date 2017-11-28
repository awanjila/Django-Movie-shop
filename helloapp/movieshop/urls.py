#movieshop/urls.py

from django.conf.urls import url
from movieshop import views

urlpatterns =[
	url(r'^$', views.index, name='index'),
	url(r'^anime/$', views.anime, name='anime'),
	url(r'^profile/$', views.profile, name='profile')

	]
