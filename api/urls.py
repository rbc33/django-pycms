from django.urls import path
from django.views.generic.base import TemplateView
from . import views


app_name = "api"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path(
        "contact/",
        TemplateView.as_view(template_name="api/contact.html"),
        name="contact",
    ),
    path("contact-send/", views.contact_send, name="contact_send"),
]
