from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Blogpost


def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})


def blogpost(request, id):
    post1 = Blogpost.objects.filter(post_id=id)[0]
    post2 = Blogpost.objects.filter(post_id=id + 1)[0]
    post3 = Blogpost.objects.filter(post_id=id - 1)[0]

    return render(request, 'blog/blogpost.html', {'post1': post1, 'post2': post2, 'post3': post3})


