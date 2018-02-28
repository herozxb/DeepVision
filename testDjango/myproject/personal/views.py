from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	#data = {'foo': 'bar', 'hello': 'world','hello2': 'world2'}
	#return HttpResponse(json.dumps(data), content_type='application/json')
    #return HttpResponse("<h2>Hello, world. You're at the personal index.</h2>")
    return render(request,'personal/home.html')
# Create your views here.