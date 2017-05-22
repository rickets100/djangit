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
    template = loader.get_template('index.html')

    return HttpResponse(template.render())

# ===== HANDLES BOTH 'GET ALL' AND 'POST ONE' =====
def hops(request):
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
    model =  {
        'hopform':hopform,
        'id': id
        }

    return render(request, 'hopform.html', model)

# ===== NEW HOP FORM =====
# django bug?
# https://code.djangoproject.com/ticket/27722?cversion=0&cnum_hist=3
def newhop(request):
    hopform = HopForm()
    # template = loader.get_template('hopform.html')
    model =  {
        'hopform':hopform
        }
    # context_instance=RequestContext(request, model)

    return render(request, 'hopform.html', model)

# ===== GET ONE BY ID =====
def onehop(request, id):
    template = loader.get_template('showhop.html')
    hop = Hop.objects.get(id=id)
    model =  {
        "hop":hop
        }

    return HttpResponse(template.render(model))

# ===== DELETE ONE =====
def deletehop(request, id):
    template = loader.get_template('hops.html')
    hop = Hop.objects.get(id=id)
    hop.delete()

    return HttpResponseRedirect('/hops/')
