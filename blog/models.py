from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок поста")
    description = models.TextField(verbose_name='Тело поста')
    technology = models.CharField(max_length=100, verbose_name='Основная '
                                                               'суть поста')
    image = models.ImageField(upload_to='static/images/blog/%Y/%m/%d',
                                 verbose_name='Изображение поста',)

    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'статьи'
