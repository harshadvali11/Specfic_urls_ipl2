from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>Ruturaj is Captain of CSK</h1>')


def vicecaptain(request):
    return HttpResponse('<h1>Jadeja is Vice Captain of CSK</h1>')

    