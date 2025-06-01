from django.shortcuts import get_object_or_404, render
from .models import Posts


# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, "api/index.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if request.htmx:
        return render(request, "api/partials/post_detail.html", {"post": post})
    return render(request, "api/post.html", {"post": post})
