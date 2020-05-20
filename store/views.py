from django.shortcuts import render
from django.http import HttpResponse
from .models import imageinfo
# Create your views here.
imageinformation = imageinfo.objects.all()


def index(request):

    params={'imageinformation': imageinformation }
    return render(request,'index.html',params);
def about(request):
    return render(request,'about.html');
def team(request):
    return render(request,'team.html');
def contect(request):
    return render(request,'contect.html');
def profile(request):
    return render(request,'profile.html');
def img2(request):
    product=imageinfo.objects.all()
    param={'product':product}
    return render(request,'img2.html',param);
def img3(request):
    product=imageinfo.objects.all()
    param={'product':product}
    return render(request,'img3.html',param);