
from django.shortcuts import render


def lovers(request):
    return render(request, 'pagelovers/pagelovers.html')
