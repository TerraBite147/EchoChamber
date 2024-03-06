from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'posted_at')
    search_fields = ['title', 'content']
    list_filter = ('status', 'posted_at')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'excerpt')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username', 'post__title')