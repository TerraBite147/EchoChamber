from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse
from django.http import JsonResponse, HttpResponseForbidden
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Post, Comment, CommentLike, PostLike
from .forms import CommentForm, PostForm

# Utility function to toggle likes for posts and comments
def toggle_like(object, user):
    if isinstance(object, Post):
        model = PostLike
    elif isinstance(object, Comment):
        model = CommentLike
    else:
        return None

    like, created = model.objects.get_or_create(user=user, **{object.__class__.__name__.lower(): object})
    if created:
        return True  # Liked
    else:
        like.delete()
        return False  # Unliked


class BlogList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-posted_at")
    template_name = "blog/index.html"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string("blog/post_list.html", context, request=request)
            return JsonResponse({"html": html})

        return self.render_to_response(context)

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()

    context = {"post": post, "comment_form": comment_form}
    return render(request, "blog/post_detail.html", context)


@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    is_liked = toggle_like(post, request.user)
    return JsonResponse({'likes_count': post.likes.count(), 'is_liked': is_liked})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.author:
        post.delete()
        return redirect('home')
    return HttpResponseForbidden("You are not allowed to delete this post.")


@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    liked = toggle_like(comment, request.user)
    updated_likes_count = CommentLike.objects.filter(comment=comment).count()
    return JsonResponse({'liked': liked, 'likes_count': updated_likes_count})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        return redirect('post_detail', slug=comment.post.slug)
    return HttpResponseForbidden("You are not allowed to delete this comment.")


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/_post_creation.html', {'form': form})