from django.shortcuts import render, get_object_or_404
from . import views
from .views import like_comment, profile
from django.urls import path

urlpatterns = [
    path("", views.BlogList.as_view(), name="home"),
    path("create/", views.create_post, name="create_post"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("post/<slug:slug>/like", views.like_post, name="like_post"),
    path("delete_post/<slug:slug>/", views.delete_post, name="delete_post"),
    path("like_comment/<int:comment_id>/", like_comment, name="like_comment"),
    path(
        "delete_comment/<int:comment_id>/", views.delete_comment, name="delete_comment"
    ),
    path("profile/", profile, name="profile"),
    path("clear-notifications/", views.clear_notifications, name="clear_notifications"),
    path(
        "notifications/read/<int:notification_id>/",
        views.read_notification,
        name="read_notification",
    ),
]
