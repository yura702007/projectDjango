from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<p>Это главная страница сайта</p>')


def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')
