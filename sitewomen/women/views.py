from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.defaultfilters import join


menu = [
    {'title': 'Главная страница', 'url_name': 'about'},
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
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html', {'title': 'О сайте', 'menu': menu})


def show_post(request: HttpRequest, post_id: int) -> HttpResponse:
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def add_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Добавление статьи</h1')


def contacts(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Обратная связь</h1')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Авторизация</h1')


def page_not_found(request: HttpRequest, exception: Exception) -> HttpResponseNotFound:
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')
