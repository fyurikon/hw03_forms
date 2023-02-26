from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
PUB_DATE_DESC: str = '-pub_date'


class Group(models.Model):
    """
    Group model is responsible for the group.
    """
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Post model is responsible for the post.
    """

    class Meta:
        ordering = [PUB_DATE_DESC]
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Группа'
    )

    def __str__(self):
        return self.text