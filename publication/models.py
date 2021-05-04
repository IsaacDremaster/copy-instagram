from django.db import models
from django.conf import settings

class Publications(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'post_owner')
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.text

class PublicationImages(models.Model):
    publication = models.ForeignKey('publication.Publications', models.CASCADE, 'post_images')
    image = models.FileField('Фотография', upload_to='post_image')
