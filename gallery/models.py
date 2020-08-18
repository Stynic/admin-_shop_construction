from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class Image(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    image = models.ImageField(blank=True,
                              upload_to='static/images/gallery/%Y/%m/%d',
                              help_text='150x150px',
                              verbose_name='Ссылка картинки')

    # Вывод картинок в админке!
    def image_img(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100"/></a>')
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'


class Video(models.Model):
    """
        Model representing a book genre (e.g. Science Fiction, Non Fiction).
        """
    video = models.FileField(upload_to='static/video/')

    class Meta:
        verbose_name = 'медиафайл'
        verbose_name_plural = 'медиафайлы'
