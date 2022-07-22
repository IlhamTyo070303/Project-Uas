from multiprocessing import context
from pyexpat import native_encoding
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'home' : '/',
        'logo': 'img/logo.png',
        'bg' : 'shop/img/oren.jpg',
        'banner': 'img/head.jpg',
        'nav1': '/',
        'nav2': '/menu',
        'nav3' : [
            ['/','Home'],
            ['/menu','Choose Your Joki!']
        
        
        ]
        ,'bgfooter' : 'shop/img/head.jpg',
        'button' : '/'
    }
    return render(request, 'jadi.html',context)