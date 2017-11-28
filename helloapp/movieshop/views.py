# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import requests
import json
from django.views.generic import TemplateView

# Create your views here.
def index(request):
	return render(request, 'index.html', context=None)

# Add this view

def anime(request):
	parsedData=[]
	req=requests.get('https://api.themoviedb.org/3/movie/900?api_key=96b0d4d8339dab13ef80edc42e9fba5b')
	jsonList=[]
	jsonList.append(json.loads(req.content))
	userData={}
	for data in jsonList:
		userData['overview'] = data['overview']
		userData['tagline'] = data['tagline']
		userData['title'] =data['title']
		userData['poster_path']=data['poster_path']
	parsedData.append(userData)

	return render(request, 'anime.html', {'data': parsedData})

def profile(request):
	return HttpResponse("coming soon with movies galore")
		
			


