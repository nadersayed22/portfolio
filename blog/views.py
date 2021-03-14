from django.shortcuts import render, get_list_or_404
from .models import post


# Create your views here.

def post_list(request):
    posts = post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, blog_id):
    post_details = post.objects.get(id=blog_id).first()
    return render(request, "blog/post_details.html", {"post": post_details})
