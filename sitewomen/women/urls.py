from django.urls import path, register_converter
from . import views, converters


register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('add_page/', views.AddPage.as_view(), name='add_page'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_posts_list, name='tag'),
]
