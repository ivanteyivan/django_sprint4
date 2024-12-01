from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(
        unique=True,
        help_text=(
            "Идентификатор страницы для URL; разрешены символы лати"
            "ницы, цифры, дефис и подчёркивание."
        ),
        verbose_name="Идентификатор")
    is_published = models.BooleanField(
        default=True,
        help_text="Снимите галочку, чтобы скрыть публикацию.",
        verbose_name="Опубликовано")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Добавлено")

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название места")
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовано")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Добавлено")

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField(
        help_text=("Если установить дату и время в будущем "
                   "— можно делать отложенные публикации."),
        verbose_name="Дата и время публикации")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор публикации")
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Местоположение")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория")
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовано")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Добавлено")

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title
