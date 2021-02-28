from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return render(request,"hello_django/jango.html")