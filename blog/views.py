from django.shortcuts import render
from .models import Post

def post(request):
    posts = Post.objects.all()
    latest_post = posts.order_by('-created_at').first()
    context = {
        'posts': posts,
        'latest_post': latest_post
    }
    return render(request, 'post.html', context)
def home_page(request):
    context = {
        'title': 'Mənim İlk Səhifəm'
    }
    return render(request, 'index.html', context)