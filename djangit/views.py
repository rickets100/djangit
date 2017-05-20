
# this is where to put the views that are called by the routes
from djangit.forms import HopForm
from djangit.models import Hop
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext, loader
import requests
from rest_framework import routers

# ===== INDEX PAGE =====
def index(request):
    print request
    print "got to index"
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# ===== GET ALL =====
def hops(request):
    print request.method
    print "got to all hops"
    all_hops = Hop.objects.all().order_by('hop_name')
    template = loader.get_template('hops.html')
    model =  {
        "all_hops":all_hops
        }
    print 'model info is'
    print model

    return HttpResponse(template.render(model))

# ===== EDIT HOP FORM =====
def edithop(request, id):
    print 'got to edithop'
    hop = Hop.objects.get(id=id)
    hopform = HopForm(instance=hop)
    model =  {
        "hopform":hopform
        }


    template = loader.get_template('hopform.html')
    return HttpResponse(template.render(model))

# ===== NEW HOP FORM =====
def newhop(request):
    print 'got to newhop'

    template = loader.get_template('hopform.html')
    return HttpResponse(template.render())

# ===== GET ONE BY ID =====
def onehop(request, id):
    print 'got to onehop'
    print request.body

    hop = Hop.objects.get(id=id)
    model =  {
        "hop":hop
        }

    template = loader.get_template('showhop.html')
    return HttpResponse(template.render(model))

# ===== DELETE ONE =====
def deletehop(request, id):
    print 'got to deletehop'

    hop = Hop.objects.get(id=id)

    template = loader.get_template('hops.html')
    return HttpResponse(template.render())
