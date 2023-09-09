from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.defaultfilters import join


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


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
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request: HttpRequest, cat_slug: str) -> HttpResponse:
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request: HttpRequest, year: int) -> HttpResponse:
    if year > 2023:
        uri = reverse('cats', args=('music',))
        return redirect(uri)
    return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')


def page_not_found(request: HttpRequest, exception: Exception) -> HttpResponseNotFound:
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')
