from django.shortcuts import render
from .models import Post


def home(request):

    all_posts = Post.newmanager.all()

    return render(request, 'index.html', {'posts': all_posts})
