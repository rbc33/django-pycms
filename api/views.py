from django.shortcuts import get_object_or_404, render
import markdown
from .models import Posts
from django.utils.safestring import mark_safe


# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, "api/index.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    post.content_html = mark_safe(
        markdown.markdown(post.content, extensions=["extra", "codehilite"])
    )

    if request.htmx:
        return render(request, "api/partials/post_detail.html", {"post": post})
    return render(request, "api/post.html", {"post": post})
