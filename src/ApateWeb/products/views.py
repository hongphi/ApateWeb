# Create your views here.
from django.contrib import auth
from django.contrib.auth import logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Product
from utils import generate_view
import math
from ApateWeb.products.forms import CommentForm
from ApateWeb.products.models import Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


def home(request):
    
    objs = generate_view(list(Product.objects.all()))
    return render_to_response('index.html',
                              {'items': objs},
                              context_instance = RequestContext(request))

@csrf_protect
def view_product(request, product_id):
    try:
        comments = Comment.objects.filter(comment_product = product_id).order_by('-comment_date')
        product = Product.objects.get(product_id = product_id)
    except Exception:
        return Http404() 
    error = None
    if request.method == "POST":
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/')

        form = CommentForm(request.POST)
        if form.is_valid():
            content = request.POST['content']
            obj = Comment(comment_content = content)
            obj.comment_user = request.user
            obj.comment_product = product
            obj.save()
            form = CommentForm()
        else:
            error = "Please input your comment"
    else:
        form = CommentForm()    
    
    return render_to_response('product.html',
                                  {'product': product, 'form': form, 'error' : error, 'comments' : comments},
                                  context_instance = RequestContext(request))
         
    
def page(req, page):
    return HttpResponse('Page: ' + page)


