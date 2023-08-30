from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Blog, Products


def blog(request):
  mymembers = Blog.objects.all().values()
  template = loader.get_template('blog.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context,request))






def products(request):
  bla = Products.objects.all().values()
  template = loader.get_template('Product_list.html')
  context = {
    'bla': bla,
  }
  return HttpResponse(template.render(context,request))