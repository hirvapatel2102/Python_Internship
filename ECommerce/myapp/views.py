from django.shortcuts import render
from .models import watch, about_us, contact

def homepageview(request):
    all_watch = watch.objects.all()[:4]
    about = about_us.objects.all()

    context = {
        'all_watch':all_watch,
        'about':about
    }
    return render(request,'home.html', context)

def aboutpageview(request):
    return render(request,'about.html')

def contactpageview(request):
    return render(request,'contact.html')

def watchview(request):
    all_watch_w = watch.objects.all()
    about_w = about_us.objects.all()

    context = {
        'all_watch_w':all_watch_w,
        'about_w':about_w,
    }
    return render(request,'watch.html', context)

