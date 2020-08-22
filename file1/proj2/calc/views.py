from django.shortcuts import render
import operator
# Create your views here.
from django.http import HttpResponse
def home(requests):
    return render(requests,'calc/home.html')
def calculate(requests):
    mytext=requests.GET['op']
    if(mytext == "add"):
        res=int(requests.GET['fno']) + int(requests.GET['sno'])
    elif(mytext == "sub"):
        res=int(requests.GET['fno']) - int(requests.GET['sno'])
    elif(mytext == "mul"):
        res=int(requests.GET['fno']) * int(requests.GET['sno'])
    elif(mytext == "div"):
        res=int(requests.GET['fno']) / int(requests.GET['sno'])
        
    else:    
        res=0
    return render(requests,'calc/calculate.html',{'result':res})
   
