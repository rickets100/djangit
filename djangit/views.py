
# this is where to put the views that are called by the routes
# one option for logging is: print request.method

from djangit.forms import HopForm
from djangit.models import Hop
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from rest_framework import routers
import requests

# ===== INDEX PAGE =====
def index(request):
    print "got to index"
    template = loader.get_template('index.html')

    return HttpResponse(template.render())

# ===== GET ALL =====
def hops(request):
    print "got to get all"
    all_hops = Hop.objects.all().order_by('hop_name')
    template = loader.get_template('hops.html')
    model =  {
        "all_hops":all_hops
        }

    return HttpResponse(template.render(model))

# ===== EDIT HOP FORM =====
def edithop(request, id):
    print 'got to edithop'
    hop = Hop.objects.get(id=id)
    hopform = HopForm(instance=hop)
    template = loader.get_template('hopform.html')
    model =  {
        "hopform":hopform
        }

    return HttpResponse(template.render(model))

# ===== NEW HOP FORM =====
def newhop(request):
    print 'got to newhop'
    hopform = HopForm()
    template = loader.get_template('hopform.html')
    model =  {
        "hopform":hopform
        }

    return HttpResponse(template.render(model))

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

# ===== ADD A HOP =====
def addhop(request, id):
    print 'got to add a shop'
    template = loader.get_template('showhop.html')
    context_instance=RequestContext(request)
    hop = Hop.objects.get(id=id)
    model =  {
        "hop":hop
        }
    model.save()

    return HttpResponse(template.render(model))

# ===== DELETE ONE =====
def deletehop(request, id):
    print 'got to deletehop'
    template = loader.get_template('hops.html')
    hop = Hop.objects.get(id=id)
    model =  {
        "hop":hop
        }
    hop.delete()

    return HttpResponse(template.render())
