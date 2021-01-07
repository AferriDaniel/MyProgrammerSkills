from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .forms import StreetName
# Create your views here.

def home(request): 
	return render(request, 'home.html')


# y='calle valentin fuster' 



def zipcode_getter(req):
	
	if req.method == 'POST':
		form = StreetName(req.POST)
		if form.is_valid():
			r = req.get(f'https://nominatim.openstreetmap.org/search?q={form}&format=json')#, params=get_params(y))
			return HttpResponse(r)
			# dump = r.json()
			# return HttpResponse(dump[0]["display_name"])
			# 
	# return HttpResponse(dump, content_type="application/json" )

	elif req.method == 'GET':
		form = StreetName()
		return render(req, 'addressform.html', {'form':form})



# def zipcode_getter(request):
	