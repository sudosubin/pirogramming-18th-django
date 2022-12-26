import traceback

from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import TemplateView

from server.apps.posts.models import Post


class PostListView(TemplateView):
    template_name = "posts/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"posts": Post.objects.all()})
        return context


class PostCreateView(TemplateView):
    template_name = "posts/create.html"

    def post(self, request: HttpRequest, *args, **kwargs):
        Post.objects.create(
            title=request.POST["title"],
            user=request.POST["user"],
            content=request.POST["content"],
            region=request.POST["region"],
            price=request.POST["price"],
        )
        return HttpResponseRedirect("/")


class PostDetailView(TemplateView):
    template_name = "posts/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(id=kwargs["pk"])
        context.update({"post": post})
        return context

    def get(self, request: HttpRequest, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Post.DoesNotExist as e:
            traceback.print_exception(e)
            return HttpResponseRedirect("/404")


class PostUpdateView(TemplateView):
    template_name = "posts/update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(id=kwargs["pk"])
        context.update({"post": post})
        return context

    def get(self, request: HttpRequest, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Post.DoesNotExist as e:
            traceback.print_exception(e)
            return HttpResponseRedirect("/404")

    def post(self, request: HttpRequest, *args, **kwargs):
        try:
            post = Post.objects.get(id=kwargs["pk"])
        except Post.DoesNotExist as e:
            traceback.print_exception(e)
            return HttpResponseRedirect("/")

        post.title = request.POST["title"]
        post.user = request.POST["user"]
        post.content = request.POST["content"]
        post.region = request.POST["region"]
        post.price = request.POST["price"]
        post.save()

        return HttpResponseRedirect("/")
