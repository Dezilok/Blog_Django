from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

posts = [
    {
        'author': 'Dezilok',
        'title': 'Post 1',
        'content': "content",
        'date_posted': '08.08.2020'
    },
    {
        'author': 'Dev',
        'title': 'Post 2',
        'content': "content",
        'date_posted': '08.08.2020'
    }
]


def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, template_name='blog/homepage.html', context=context)


def about(request):
    return render(request, template_name='blog/about.html', context={'title': 'About'})
