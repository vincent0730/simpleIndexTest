from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#编写视图
#home_page = None

def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')