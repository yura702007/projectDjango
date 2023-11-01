from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, Women


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = """
    АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- 
    """
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел."

    def __call__(self, value):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code, params={'value': value})


class AddPostForm(forms.ModelForm):
    # title = forms.CharField(
    #     max_length=255,
    #     min_length=5,
    #     required=True,
    #     label='Заголовок',
    #     widget=forms.TextInput(attrs={'class': 'form-input'}),
    #     error_messages={
    #         'min_length': 'Слишком короткий заголовок',
    #         'required': 'Без заголовка никак'
    #     },
    #     # validators=[RussianValidator()]
    # )
    # slug = forms.SlugField(
    #     max_length=255,
    #     label='URL',
    #     validators=[MinLengthValidator(5), MaxLengthValidator(100)]
    # )
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Контент')
    # is_published = forms.BooleanField(required=False, label='Статус', initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label="Категории")
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(), empty_label="Не замужем", required=False, label="Муж"
    )

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'cat', 'husband', 'is_published', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        allowed_chars = """
            АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- 
            """
        if not set(title) <= set(allowed_chars):
            raise ValidationError("Должны присутствовать только русские символы, дефис и пробел.")
        return title

    # def clean_cat(self):
    #     cat = self.cleaned_data['cat']
    #     print(cat)
    #     return cat


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')
