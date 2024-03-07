from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, CommentLike, PostLike


# Create your views here.


class BlogList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-posted_at")
    template_name = "blog/index.html"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            # Render the posts only, not the full page
            html = render_to_string(
                "blog/post_list.html",
                context,
                request=request,
            )
            # Return the HTML as JSON
            return JsonResponse({"html": html})

        # For non-AJAX requests, render the full page as usual
        return self.render_to_response(context)


def post_detail(request, slug):
    """
    View for individual post

    **context**
    post : an instance of Post model

    **template**
    blog/post_detail.html

    """
    queryset = Post.objects.filter(status=1).order_by("-posted_at")
    post = get_object_or_404(queryset, slug=slug)
    # comments = post.comments.filter(active=True)
    return render(request, "blog/post_detail.html", {"post": post})


def like_post(request, slug):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=403)

    post = get_object_or_404(Post, slug=slug)
    liked, created = PostLike.objects.get_or_create(post=post, user=request.user)
    
    if not created:  # The like already exists, so remove it
        liked.delete()
        is_liked = False
    else:
        is_liked = True

    return JsonResponse({'likes_count': post.likes.count(), 'is_liked': is_liked})


def unlike_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    PostLike.objects.filter(post=post, user=request.user).delete()
    return redirect("post_detail", post_id=post.id)
