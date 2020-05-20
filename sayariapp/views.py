from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import sayariinfo

def sayariapp(request):
    sayari=sayariinfo.objects.all()
    param={'sayari':sayari}
    return render(request,'sayari/index.html',param);
def sad(request):
    sayari = sayariinfo.objects.all()
    param = {'sayari': sayari}


    return render(request, 'sayari/sad.html',param);
def romantic(request):



    return render(request, 'sayari/romantic.html');

def sabout(request):
    return render(request,'sayari/about.html');
def steam(request):
    return render(request,'sayari/team.html');
def scontect(request):
    return render(request,'sayari/contect.html');
def sprofile(request):
    return render(request,'sayari/profile.html');
