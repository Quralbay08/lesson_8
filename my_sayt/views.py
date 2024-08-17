from . import models
from django.shortcuts import render,get_object_or_404


def homepage(request):
    blog = models.Blogs.objects.all()
    return render(request,'home.html',{'bloglar':blog})

def product_detail(request):
    blog = models.Blogs.objects.all()
    return render(request,'detail.html',{'detail':blog})




