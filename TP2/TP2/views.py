from django.shortcuts import render
from django.contrib.auth.models import User
from api.models import Post


def index(request):
    posts = Post.objects.all()
    users = User.objects.all()
    context = {
        "posts":posts,
        "users":users
    }   
    return render(request, 'TP2/index.html', context)