from django.shortcuts import render

def index(request):
    return render(request, '.\pages\index.html')


def contact(request):
    return render(request, '.\pages\contact.html')


def product_list(request):
    return render(request, '.\pages\product_list.html')


def product(request):
    return render(request, '.\pages\product.html')