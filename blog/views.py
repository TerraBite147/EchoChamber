from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from django.http import JsonResponse
from django.template.loader import render_to_string


# Create your views here.


class BlogList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-posted_at')
    template_name = 'blog/index.html'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Render the posts only, not the full page
            html = render_to_string(
                'blog/post_list.html', 
                context,
                request=request,
            )
            # Return the HTML as JSON
            return JsonResponse({'html': html})

        # For non-AJAX requests, render the full page as usual
        return self.render_to_response(context)
