from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.TextField('Название')
    anons = models.TextField('Анонс')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Новость: {self.title}'

    def get_absolute_url(self):
        return '/news'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
