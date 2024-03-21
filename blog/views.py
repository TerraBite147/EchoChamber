from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse
from django.http import JsonResponse, HttpResponseForbidden
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.text import slugify
from .models import Post, Comment, CommentLike, PostLike, Notification, Category
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.db.models import Count


# Utility function to toggle likes for posts and comments
def toggle_like(object, user):
    if isinstance(object, Post):
        model = PostLike
    elif isinstance(object, Comment):
        model = CommentLike
    else:
        return None

    like, created = model.objects.get_or_create(
        user=user, **{object.__class__.__name__.lower(): object}
    )

    if created:
        if isinstance(object, Comment):
            object.likes.add(user)
        return True  # Liked
    else:
        like.delete()
        if isinstance(object, Comment):
            object.likes.remove(user)
        return False  # Unliked


class BlogList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.GET.get("category", None)
        sort = self.request.GET.get("sort", "date")

        if category_name:
            queryset = queryset.filter(category__name=category_name)

        if sort == "likes":
            queryset = queryset.annotate(like_count=Count("likes")).order_by(
                "-like_count"
            )
        elif sort == "comments":
            queryset = queryset.annotate(comment_count=Count("comments")).order_by(
                "-comment_count"
            )
        else:  # Default to sort by date
            queryset = queryset.order_by("-posted_at")

        return queryset

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            page = request.GET.get("page")
            paginator = Paginator(self.object_list, self.paginate_by)

            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)

            html = render_to_string(
                "blog/_post_list_partial.html",
                {"post_list": posts},
                request=request,
            )
            return JsonResponse({"html": html, "has_next": posts.has_next()})

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    comment_form = CommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect("post_detail", slug=post.slug)
        else:
            # Redirect unauthenticated users to the login page
            return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))

    context = {"post": post, "comment_form": comment_form}
    return render(request, "blog/post_detail.html", context)


@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    is_liked = toggle_like(post, request.user)

    # Create a notification if the post is liked (not unliked)
    if is_liked:
        Notification.objects.create(
            user=post.author,
            message=f"Your post '{post.title}' received a new like!",
            target_url=reverse("post_detail", kwargs={"slug": post.slug}),
        )

    return JsonResponse({"likes_count": post.likes.count(), "is_liked": is_liked})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect("home")
    else:
        return HttpResponseForbidden("You are not allowed to delete this post.")


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()

            # Check if the post is a draft
            if post.status == 0: 
                # Redirect to the profile page if the post is a draft
                return redirect("profile")
            else:
                # Redirect to the post detail page if the post is published
                return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm()
    return render(request, "blog/_post_creation.html", {"form": form})


@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author and not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            edited_post = form.save() 
            if edited_post.status == 0:
                return redirect("profile")
            else:
                return redirect("post_detail", slug=edited_post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/_post_edit.html", {"form": form, "post": post})


@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    liked = toggle_like(comment, request.user)
    updated_likes_count = CommentLike.objects.filter(comment=comment).count()
    return JsonResponse({"liked": liked, "likes_count": updated_likes_count})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
        return redirect("post_detail", slug=comment.post.slug)
    else:
        return HttpResponseForbidden("You are not allowed to delete this comment.")


@login_required
def profile(request):
    user_posts = (
        Post.objects.filter(author=request.user, status=1)
        .annotate(comment_count=Count("comments"), like_count=Count("likes"))
        .order_by("-posted_at")
    )

    draft_posts = Post.objects.filter(author=request.user, status=0).order_by(
        "-posted_at"
    )

    user_comments = (
        Comment.objects.filter(author=request.user)
        .annotate(likes_count=Count("likes"))
        .order_by("-created_at")
    )

    user_notifications = Notification.objects.filter(
        user=request.user, is_read=False
    ).order_by("-created_at")

    has_unread_notifications = user_notifications.exists()

    context = {
        "user_posts": user_posts,
        "draft_posts": draft_posts,
        "user_comments": user_comments,
        "user_notifications": user_notifications,
        "has_unread_notifications": has_unread_notifications,
    }

    return render(request, "blog/_profile.html", context)


@login_required
def read_notification(request, notification_id):
    notification = get_object_or_404(
        Notification, id=notification_id, user=request.user
    )
    notification.is_read = True
    notification.save()
    return redirect(notification.target_url)


@login_required
def clear_notifications(request):
    Notification.objects.filter(user=request.user).update(is_read=True)
    return redirect("profile")


def about(request):
    return render(request, "blog/about.html")
