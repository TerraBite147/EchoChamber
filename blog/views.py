from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Post, Comment, CommentLike, PostLike
from .forms import CommentForm, PostForm


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
    - post : an instance of Post model
    - comment_form : a form for adding a new comment

    **template**
    - blog/post_detail.html

    """
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

    context = {
        "post": post,
        "comment_form": comment_form,
    }
    return render(request, "blog/post_detail.html", context)


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



@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    # Check if the user has already liked this comment
    like, created = CommentLike.objects.get_or_create(user=request.user, comment=comment)

    if not created:
        # If the like already exists, delete it (unlike action)
        like.delete()
        liked = False
    else:
        # If the like is new, just mark it as liked
        liked = True

    # Re-query to get the updated likes count after the like/unlike action
    updated_likes_count = CommentLike.objects.filter(comment=comment).count()

    return JsonResponse({
        'liked': liked,
        'likes_count': updated_likes_count,
    })
    
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # Ensure the request user is the author of the comment
    if request.user == comment.author:
        comment.delete()
        # Redirect back to the post detail page
        return redirect('post_detail', slug=comment.post.slug)
    else:
        # Handle unauthorized attempts
        return HttpResponseForbidden("You are not allowed to delete this comment.")
    
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the current user
            post.slug = slugify(post.title)  # Generate a slug from the title
            post.save()
            return redirect('post_detail', slug=post.slug)  # Redirect to the post's detail view
    else:
        form = PostForm()

    return render(request, 'blog/_post_creation.html', {'form': form})