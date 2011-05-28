# Create your views here.
from django.contrib import auth
from django.contrib.auth import logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Product
from utils import generate_view
import math


def home(request):
    
    objs = generate_view(list(Product.objects.all()))
    return render_to_response('index.html',
                              {'items': objs},
                              context_instance = RequestContext(request))

def view_product(request, product_id):
    try:
        product = Product.objects.get(product_id = product_id)
        
        return render_to_response('product.html',
                                  {'product': product},
                                  context_instance = RequestContext(request))
    except Exception:
        return Http404() 
    
    

def page(req, page):
    return HttpResponse('Page: ' + page)


