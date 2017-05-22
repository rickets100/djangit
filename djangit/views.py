
# this is where to put the views that are called by the routes
# one option for logging is: print request.method

from djangit.forms import HopForm
from djangit.models import Hop
from django.shortcuts import render_to_response
from django.shortcuts import render
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
    print "request.method is"
    print request.method

    if request.method == 'GET':
        all_hops = Hop.objects.all().order_by('hop_name')
        template = loader.get_template('hops.html')
        model =  {
            "all_hops":all_hops
            }
        return HttpResponse(template.render(model))
    else:
        # request method was POST
        form = HopForm(request.POST)
        template = loader.get_template('hops.html')
        form.save()

        return HttpResponseRedirect('/hops/')


# ===== EDIT HOP FORM =====
def edithop(request, id):
    print 'got to edithop'
    hop = Hop.objects.get(id=id)
    hopform = HopForm(instance=hop)
    # template = loader.get_template('hopform.html')
    model =  {
        'hopform':hopform,
        'id': id
        }
    # context_instance=RequestContext(request, model)

    return render(request, 'hopform.html', model)

# ===== NEW HOP FORM =====
# django bug?
# https://code.djangoproject.com/ticket/27722?cversion=0&cnum_hist=3
def newhop(request):
    print 'got to newhop'
    hopform = HopForm()
    # template = loader.get_template('hopform.html')
    model =  {
        'hopform':hopform
        }
    # context_instance=RequestContext(request, model)

    return render(request, 'hopform.html', model)

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

# ===== ADD A NEW HOP =====
def addhop(request):
    print 'got to addhop'
    print 'request body is'
    print request.body

    template = loader.get_template('hops.html')
    # hop = Hop.objects.get()
    # model =  {
    #     "hop":hop
    #     }
    # hop.save()

    return HttpResponse(template.render())

# ===== DELETE ONE =====
def deletehop(request, id):
    print 'got to deletehop'
    template = loader.get_template('hops.html')
    all_hops = Hop.objects.all().order_by('hop_name')
    hop = Hop.objects.get(id=id)
    hop.delete()
    model =  {
        "all_hops":all_hops
        }

    return HttpResponse(template.render(model))
