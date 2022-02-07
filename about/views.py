from django.shortcuts import render
from django.views import View

def About(request):
    return render(request, 'about/about.html')
