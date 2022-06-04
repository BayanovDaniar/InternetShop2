from django.shortcuts import render

def productpage(request):
    return render(request, 'productpage/product.html')


