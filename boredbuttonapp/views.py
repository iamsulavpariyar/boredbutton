from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect, HttpResponse
from .models import Contact
from .models import Games
from .models import *




# Create your views here.


def home(request):
    
    return render(request , 'home/index.html')

def games(request):
    allgames = Games.objects.all()
    context = {'allgames': allgames}   
    return render(request , 'games/index.html',context)

def contact(request):
        
    if request.method=='POST':
        siteurl = request.POST['link']
        shortdis = request.POST['comments']
        email = request.POST['email']
        print(siteurl, shortdis, email)
        contact = Contact(siteurl=siteurl, shortdis=shortdis, email=email)
        contact.save()
    
    return render(request , 'home/contact.html')
    

def base(request, slug):
    ongame = Games.objects.filter(slug=slug).first()
    context = { "ongame": ongame}
    return render(request, 'base.html', context) 

# def base(request, slug):
   # ongames = Games.objects.filter(slug=slug).first
  #  context = {'ongames': ongames}   
   #  return render(request , 'base.html',context)





