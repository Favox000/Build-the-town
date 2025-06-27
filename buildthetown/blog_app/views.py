from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.utils import timezone
from django.contrib.auth.views import LogoutView

# Create your views here.


def index(request):
    return render(request, "blog_app/index.html")

def all_post(request):
    posts = BlogPost.objects.filter(
        visible=True,
        issue_date__lte=timezone.now()
    ).order_by('-issue_date')
    return render(request, "blog_app/all-post.html", {
        "articles": posts
    })

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, "blog_app/blog-detail.html", {
        "post": post
    })

def rules(request):
    return render(request, "rules.html")