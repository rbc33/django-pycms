from django.urls import path
from . import views


app_name = "api"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
]
