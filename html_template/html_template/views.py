from django.shortcuts import render        
from django.http import HttpResponse
        
def about(request):    
    return HttpResponse('<h1>This is about me!.</h1>') 

def index(request):
    return render(request, 'index.html')