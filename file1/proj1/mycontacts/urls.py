from django.contrib import admin
from django.urls import path
from django.conf.urls import include , url
from mycontacts import views

urlpatterns=[url(r'contact1.*',views.contact1,name='contact1'),
			url(r'contact2.*',views.contact2,name='contact2'),
            
			]