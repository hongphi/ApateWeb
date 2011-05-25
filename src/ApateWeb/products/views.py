# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from ApateWeb.products.models import Product
import math
from django.contrib.auth import logout
from django.contrib import auth


def home(request):
    objs = generate(list(Product.objects.all()))
    return render_to_response('index.html',
                              {'items': objs},
                              context_instance = RequestContext(request))

def generate(objs):
    objs_len = len(objs)
    lst = []
    row = objs_len >> 2
    for i in range(row):
        temp = []
        temp.append(objs[i << 2])
        temp.append(objs[(i << 2) + 1])
        temp.append(objs[(i << 2) + 2])
        temp.append(objs[(i << 2) + 3])
        lst.append(temp)

    if objs_len % 4 != 0:
        odd = objs_len % 4 - 1
        count = 0
        temp = []
        while odd >= count:
            temp.append(objs[(row << 2) + count])
            count += 1

        while len(temp) < 4:
            temp.append(None)

        lst.append(temp)

    return lst

def page(req, page):
    return HttpResponse('Page: ' + page)


