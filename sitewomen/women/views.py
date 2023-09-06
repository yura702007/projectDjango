from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<p>Это главная страница сайта</p>')


def categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Статьи по категориям</h1>')
