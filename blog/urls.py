from django.shortcuts import render, get_object_or_404
from . import views
from django.urls import path

urlpatterns = [
    path("", views.BlogList.as_view(), name="home"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
]
