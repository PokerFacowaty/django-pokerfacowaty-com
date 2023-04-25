from django.shortcuts import render, HttpResponse, redirect
from .models import PaMLPage
from blog.models import BlogPost
from paml2html import convert_from_text


def index(request):
    posts = BlogPost.objects.filter(VISIBILITY='PU').order_by('-PUBLISHED')[:5]
    return render(request, 'pages/base_main.html', {'posts': posts})


def archive(request):
    return render(request, 'pages/base_archive.html')


def dating(request):
    return render(request, 'pages/base_dating.html',
                           {'css': 'pages/css/dating.css',
                            'css_dark': 'pages/css/dating_dark.css'})


def pamlpage(request, short):
    if PaMLPage.objects.get(SHORT_TITLE=short).VISIBILITY == "PR":
        if not request.user.is_authenticated:
            return redirect("/admin/")
    title = PaMLPage.objects.get(SHORT_TITLE=short).TITLE
    raw_paml = PaMLPage.objects.get(SHORT_TITLE=short).PAML_CONTENT
    converted = convert_from_text(raw_paml)
    return render(request, 'pages/base_paml.html',
                           {'paml': converted,
                            'title': title,
                            'css': f'pages/css/{short}.css',
                            'css_dark': f'pages/css/{short}_dark.css'})
