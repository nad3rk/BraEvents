""" Views """

from django.shortcuts import render

# Create your views here.

def home(request):
    """ Home """
    context = {}

    return render(request, 'app/index.html', context)

def imprint(request):
    """ Investoren """
    context = {}

    return render(request, 'app/imprint.html', context)

def dataprivacy(request):
    """ Investoren """
    context = {}

    return render(request, 'app/dataprivacy.html', context)