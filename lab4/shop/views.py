from django.shortcuts import render

def home(request):
    return render(request, "shop/home.html", {"title": "Магазин одягу"})

def men(request):
    return render(request, "shop/men.html", {"title": "Чоловічий одяг"})

def women(request):
    return render(request, "shop/women.html", {"title": "Жіночий одяг"})

def kids(request):
    return render(request, "shop/kids.html", {"title": "Дитячий одяг"})

def about(request):
    return render(request, "shop/about.html", {"title": "Про магазин"})
