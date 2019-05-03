from django.shortcuts import render,loader,HttpResponse
from vetodemo import models

# Create your views here.

def home_view(request):
    template = loader.get_template('main/home.html')
    items=models.Popular_videos.objects.filter(category__category_name='PSC')
    return HttpResponse(template.render({'items':items}, request))

def home2_view(request):
    template = loader.get_template('main/home2.html')
    items=models.Popular_videos.objects.filter(category__category_name='PSC')
    return HttpResponse(template.render({'items':items}, request))