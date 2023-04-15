from django.shortcuts import render, HttpResponse
from .models import BlogPost
from paml2html import convert_from_text


def index(request):
    posts = BlogPost.objects.filter(VISIBILITY='PU').order_by('-PUBLISHED')
    return render(request, 'blog/base_main.html', {'posts': posts})


def post(request, short):
    post = BlogPost.objects.get(SHORT_TITLE=short)
    raw_paml = BlogPost.objects.get(SHORT_TITLE=short).PAML_CONTENT
    converted = convert_from_text(raw_paml)
    return render(request, 'blog/base_post.html', {'post': post,
                                                   'paml': converted})
