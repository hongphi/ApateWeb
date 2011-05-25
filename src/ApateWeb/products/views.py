# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from ApateWeb.products.models import Product
import math
from django.contrib.auth import logout
from django.contrib import auth


def home(request):
    objs = Product.objects.all()
    return render_to_response('index.html',
                              {'items': objs},
                              context_instance = RequestContext(request))

def page(req, page):
    return HttpResponse('Page: ' + page)

#def login(req):
#    if req.method == "POST":
#        username = req.POST.get('username', '')
#        password = req.POST.get('password', '')
#        user = auth.authenticate(username = username, password = password)
#        if user:
#            auth.login(req, user)
#            
#
#def logout(req):
#    logout(req)
#    return HttpResponseRedirect('/')
#def home(request):
#    values = request.META.items()
#    s = []
#    for k, v in values:
#        s.append('%s: %s<br>' % (k, v))
#    return HttpResponse("Hello, World!!<br>" + ''.join(s) +
#
#                        request.META['HTTP_USER_AGENT'] + "<br>" +
#                        request.META['REMOTE_ADDR'] + "<br>")
#    return render_to_response('index.html',
#                              {'text': "Hello, World!!"},
#                              context_instance = RequestContext(request))


