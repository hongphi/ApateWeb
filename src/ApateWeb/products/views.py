# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Product
from utils import generate_view, generate_select_page
from ApateWeb.products.forms import CommentForm
from ApateWeb.products.models import Comment
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

def index(request):
    return HttpResponseRedirect("/products/1/")

def home(request, page):
    page = int(page)
    total = Product.objects.count()
    n = settings.PRODUCT_OF_PAGE
    pages = total / n
    if total % n != 0:
        pages += 1
        
    if page > pages:
        raise Http404()
    offset_from = (page - 1) * n
    offset_to = offset_from + n

    objs = generate_view(list(Product.objects.all()[offset_from:offset_to]))
    return render_to_response('index.html',
                              {'items': objs,
                               'current': page,
                               'pages': generate_select_page(pages, page)},
                              context_instance = RequestContext(request))

@csrf_protect
def view_product(request, product_id):
    try:
        comments = Comment.objects.filter(comment_product = product_id).order_by('-comment_date')
        product = Product.objects.get(product_id = product_id)
    except Exception:
        raise Http404()
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


