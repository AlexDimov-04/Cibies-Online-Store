from django.http import HttpResponse
from django.shortcuts import render

def indexx(request):
    return HttpResponse('12345')
