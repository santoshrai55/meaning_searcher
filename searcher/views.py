from django.shortcuts import render
from . import searcher

# Create your views here.


def searchbox(request):
    # worker = []
    # if not keyboard.is_pressed(hotkey):
    #     ideal = {'term': "",
    #              'final_term': "Click shift+F1 to search the term in your clipboard."}
    #     return render(request, 'searcher/home.html', {'worker': ideal})

    worker = searcher.searcher()

    return render(request, 'searcher/home.html', {'worker': worker})
