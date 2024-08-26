from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#What do I want the client to see?
#Send html files to the client

#Create first funtion 
def hello(request):
    return HttpResponse('Hello Word')

def about(reques):
    return HttpResponse('About')