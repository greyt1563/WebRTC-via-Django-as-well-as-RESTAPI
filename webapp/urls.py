from django.contrib import admin
from django.urls import path, include
from webapp import views
from django.http import HttpResponse

urlpatterns = [
    path("", views.index, name="home"),
    path("ui", views.ui, name="ui"),
]
