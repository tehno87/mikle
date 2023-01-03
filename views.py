

from django.http import HttpResponse
from django.shortcuts import render  # new

def home(request):
    return render(request, 'home.html')  # new
