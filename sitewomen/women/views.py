from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.defaultfilters import join

from .models import Women, Category

menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contacts'},
    {'title': 'Авторизация', 'url_name': 'login'},
]


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_publisher': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_publisher': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_publisher': True},
]


def index(request: HttpRequest) -> HttpResponse:
    posts = Women.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request: HttpRequest, post_slug: str) -> HttpResponse:
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1
    }
    return render(request, 'women/post.html', data)


def show_category(request: HttpRequest, cat_slug: str) -> HttpResponse:
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=data)


def add_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Добавление статьи</h1')


def contacts(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Обратная связь</h1')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Авторизация</h1')


def page_not_found(request: HttpRequest, exception: Exception) -> HttpResponseNotFound:
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')
