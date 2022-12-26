from django.urls import path
from django.http import HttpResponse

from server.apps.posts import views

app_name = "posts"

urlpatterns = [
    path("health", lambda *args, **kwargs: HttpResponse("hi")),
]
