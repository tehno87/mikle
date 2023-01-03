# from django.http import HttpResponse
#
# def about(request):
#     return HttpResponse('This is about page')
#
# # def home(request):
# #     return HttpResponse('My home')
#
#
# def home(request):
#     return render(request, 'home.html')


from django.http import HttpResponse
from django.shortcuts import render  # new


def about(request):
    return HttpResponse('This is about page')


def home(request):
    return render(request, 'home.html', {'greeting': 'hello'})  # new
