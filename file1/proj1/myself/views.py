from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import operator
def home(requests):
    return HttpResponse('<h1> This is first page</h1>')
