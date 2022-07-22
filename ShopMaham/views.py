from multiprocessing import context
from pyexpat import native_encoding
from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    context = {
    
        'home': '/',
        'logo': 'img/logo.png',
        'icon': 'img/logo.png',
        'banner': 'shop/img/head.jpg',
        'page': 'Home',
        'nav1': '/',
        'nav2': '/menu',
        'nav3' : [
            ['/','Home'],
            ['/menu','Choose Your Joki!']
        
        ]
        ,'image' : 'img/depan.png'
        ,'bgfooter' : 'shop/img/head.jpg',
    }
    return render(request, 'base.html',context)

