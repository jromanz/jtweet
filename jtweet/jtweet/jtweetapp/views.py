from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.

def index(request):
	return render_to_response('jtweetapp/index.html',{},context_instance=RequestContext(request))