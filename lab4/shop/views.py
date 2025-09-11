from django.shortcuts import render

def home(request):
    return render(request, "shop/home.html")

def men(request):
    return render(request, "shop/men.html")

def women(request):
    return render(request, "shop/women.html")

def kids(request):
    return render(request, "shop/kids.html")

def about(request):
    return render(request, "shop/about.html")

