from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def guest(request):
    return render(request, 'guest.html', {})

def groom_bride(request):
    return render(request, 'groom-bride.html', {})

def when_where(request):
    return render(request, 'when_where.html', {})
