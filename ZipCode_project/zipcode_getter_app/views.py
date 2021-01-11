from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .forms import StreetName
# Create your views here.

def home(request): 
	return render(request, 'home.html')


def get_query(q):
	return q.replace(" ","+")


def zipcode_getter(request):

	if request.method=="GET":
		form=StreetName()
		return render(request, 'addressform.html', {'form':form})

	elif request.method=="POST":
		address_name=request.POST["address_name"]
		url= f"https://nominatim.openstreetmap.org/search?q={get_query(address_name)}&format=json"
		r=requests.get(url).json()
		dump=json.dumps(r[0]["display_name"].split(",")[7].strip())
		return HttpResponse(dump,content_type="application/json")


