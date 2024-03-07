from django.shortcuts import render, get_object_or_404
from . import views
from django.urls import path

urlpatterns = [
    path("", views.BlogList.as_view(), name="home"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path('post/<slug:slug>/like', views.like_post, name='like_post'),
    path('post/<int:post_id>/like', views.like_post, name='like_post'),
    path('post/<int:post_id>/unlike', views.unlike_post, name='unlike_post'),
]
