from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def abc(request):
    return HttpResponse("<html>This is abc.</html>")

def index(request):
    return HttpResponse("<html>Hello, world. You're at the <b>Spider</b> index.</html>")
