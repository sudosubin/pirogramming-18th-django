from django.urls import path

from server.apps.posts import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view()),
    path("post/create/", views.PostCreateView.as_view()),
    path("post/<int:pk>/", views.PostDetailView.as_view()),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view()),
]
