from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('gen', views.gen, name="gen"),
    path('copy/<str:ena>', views.copy, name="copy")
]
