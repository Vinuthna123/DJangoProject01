from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import operator
def contact1(requests):
    return HttpResponse('Hello there, this is my first contact')
def contact2(requests):
    return HttpResponse('This is page of second contact')
