from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        help_text='Имя',
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        help_text='Фамилия',
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='Электронная почта',
        unique=True,
    )
    username = models.CharField(
        verbose_name='Username',
        help_text='Username',
        max_length=150,
        unique=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)


class SubscribeUser(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='subscribes',
        verbose_name='Подписки',
        help_text='Подписки'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='subscribe',
        verbose_name='Автор',
        help_text='Автор, на которого подписаны'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_subscribe'
            ),
            models.CheckConstraint(
                check=~(models.Q(user=models.F('author'))),
                name='user_is_not_author'
            ),
        )
