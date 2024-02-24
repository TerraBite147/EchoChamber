from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'posted_at')
    search_fields = ['title', 'content']
    list_filter = ('status', 'posted_at')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'excerpt')


# Register your models here.

admin.site.register(Category)
