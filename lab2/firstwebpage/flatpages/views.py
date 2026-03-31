from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'templates/index.html')

def static_handler(request):
    return render(request, 'templates/static_handler.html')

def home_text(request):
    return HttpResponse(u'Привет, Мир!', content_type="text/plain")

def home_text_default(request):
    return HttpResponse(u'Привет, Мир!')
