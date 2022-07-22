from tkinter import Menu
from django.shortcuts import render
from logging import _STYLES
from tkinter.ttk import Style
from webbrowser import BackgroundBrowser

# Create your views here.
def index(request):
    context = {
        'home' :'/',
        'img1' : 'shop/img/reihan.jpg',
        'nama1' : 'Nama : Reihan Babe Destroyer',
        'skill1' : 'Skill : Berubah bentuk, Mobile Legends',
        'rate1' : 'Rating : 7/10',
        'no1' : 'Harga : Rp 50.000 per mapel',

        'img2' : 'shop/img/tyo.jpg',
        'nama2' : 'Nama : Tyo The Saddest Boy',
        'skill2' : 'Skill : Menangis, Matematika',
        'rate2' : 'Rating : 8/10',
        'no2' : 'Harga : Rp 50.000 per mapel',
        
        'img3' : 'shop/img/tegar.jpg',
        'nama3' : 'Nama : Tegar The Waifu Hunter',
        'skill3' : 'Skill : Tertawa, Memasak ',
        'rate3' : 'Rating : 7.5/10',
        'no3' : 'Harga : Rp 50.000 per mapel',
        
        'img4' : 'shop/img/enri.jpg',
        'nama4' : 'Nama : Enri Naxz Bekonang',
        'skill4' : 'Skill : Mengadu domba, Tersenyum',
        'rate4' : 'Rating : 9/10',
        'no4' : 'Harga : Rp 50.000 per mapel',

        'img5' : 'shop/img/marpaung.jpeg',
        'nama5' : 'Nama : Marpaung Hitz',
        'skill5' : 'Skill : Klarifikasi, Menghabiskan Nasi',
        'rate5' : 'Rating : 8/10',
        'no5' : 'Harga : Rp 50.000 per mapel',

        'logo': 'img/logo.png',
        'banner': 'shop/img/head.jpg',
        'page': 'Choose Your Joki',
        'nav3' : [
            ['/','Home'],
        ],
        'bgfooter' : 'shop/img/head.jpg',
        'menu' : '/jadi'
    }
    
    return render(request, 'menu.html', context)

