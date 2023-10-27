from django import forms
from .models import Category, Husband


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        min_length=5,
        required=True,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        error_messages={
            'min_length': 'Слишком короткий заголовок',
            'required': 'Без заголовка никак'
        }
    )
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Контент')
    is_published = forms.BooleanField(required=False, label='Статус', initial=True)
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана'
    )
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(), required=False, label='Муж', empty_label='Не замужем'
    )
