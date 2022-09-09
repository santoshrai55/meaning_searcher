from django.shortcuts import render
from . import searcher

# Create your views here.


def searchbox(request):
    worker = searcher.searcher()
    return render(request, 'searcher/home.html', {'worker': worker})
