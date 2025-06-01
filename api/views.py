from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.utils.safestring import mark_safe
import markdown
from .models import Posts
from .forms import ContactForm


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


@require_POST
def contact_send(request):
    """Handle the contact form submission"""
    form = ContactForm(request.POST)

    # Get form values for potential error display
    email = request.POST.get("email", "")
    name = request.POST.get("name", "")

    if form.is_valid():
        # All validation passed
        email = form.cleaned_data["email"]
        name = form.cleaned_data["name"]
        message = form.cleaned_data["message"]

        # Here you could send an email or save to database
        # send_contact_email(name, email, message)

        # Return success response
        return render(
            request,
            "api/contact_success.html",
            {
                "email": email,
                "name": name,
            },
        )
    else:
        # Form validation failed - check which field failed
        error_message = ""

        # Find the first error message to display
        if "email" in form.errors:
            error_message = form.errors["email"][0]
        elif "name" in form.errors:
            error_message = form.errors["name"][0]
        elif "message" in form.errors:
            error_message = form.errors["message"][0]
        else:
            # Handle any non-field errors
            error_message = (
                form.non_field_errors()[0]
                if form.non_field_errors()
                else "An unknown error occurred"
            )

        # Return failure response
        return render(
            request,
            "api/contact_failure.html",
            {
                "email": email,
                "error": error_message,
            },
        )
