from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Post,User

# Create your views here.

def index(request):
	posts=Post.objects.all()
    template = loader.get_template('blogger/index.html')
    context = RequestContext(request, {
        'posts': posts,
    })
    return HttpResponse(template.render(context))