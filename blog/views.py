from django.shortcuts import render
from django.views import generic
from .models import Post, Comment

# Create your views here.


class BlogList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'blog/blog_list.html'
