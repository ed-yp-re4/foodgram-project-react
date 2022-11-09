from django.db import models


class Tag(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Название',
        unique=True,
    )
    color = models.CharField(
        max_length=7,
        verbose_name='Цвет',
        help_text='Цвет',
        unique=True,
    )
    slug = models.SlugField(
        max_length=200,
        verbose_name='Slug',
        help_text='Slug',
        unique=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Тег',
        verbose_name_plural = 'Теги',
        ordering = ('slug',)

    def __str__(self):
        return f'Tag: {self.slug}-{self.color}'

    def __repr__(self):
        return f'Tag: {self.slug}-{self.color}'
