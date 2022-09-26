from django.shortcuts import render

def index(request):
    return render(request, 'Home/index.html')

def about(request):
    return render(request, 'Home/about.html')

def regression(request):
    return render(request, 'Home/regression.html')

def classification(request):
    return render(request, 'Home/classification.html')