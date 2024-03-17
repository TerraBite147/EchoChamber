from django.shortcuts import render, get_object_or_404
from . import views
from .views import like_comment
from django.urls import path

urlpatterns = [
    path("", views.BlogList.as_view(), name="home"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path('post/<slug:slug>/like', views.like_post, name='like_post'),
    path('like_comment/<int:comment_id>/', like_comment, name='like_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('create/', views.create_post, name='create_post'),
    
]
