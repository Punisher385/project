from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("men/", views.men, name="men"),
    path("women/", views.women, name="women"),
    path("kids/", views.kids, name="kids"),
    path("about/", views.about, name="about"),
]
