from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import operator
def home(requests):
    return HttpResponse('<h1> This is first page</h1>')
def about(requests):
    return HttpResponse('<h1> Hi, I am Vinuthna</h1>')
def hobbies(requests):
    return HttpResponse('<h1> Reading books, playing shuttle, Sketching</h1>)
