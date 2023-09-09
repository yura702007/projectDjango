from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return self.a


def index(request: HttpRequest) -> HttpResponse:
    data = {
        'tittle': 'Главная страница',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'asd', True],
        'set': {1, 2, 3, 4, 5},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20)
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'women/about.html', {'tittle': 'О сайте'})


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
