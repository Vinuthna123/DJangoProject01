from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import operator
def drinks(requests):
    return HttpResponse('Drink 3 L water everyday to avoid any problems')
def foods(requests):
    return HttpResponse('Do not eat junk food as it may harm you and cause obesity')
