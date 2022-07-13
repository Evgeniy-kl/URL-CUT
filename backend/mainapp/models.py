from django.contrib.auth.models import AbstractUser
from django.db import models


class ShortUrl(models.Model):
    target_url = models.URLField(verbose_name='target_url')
    url = models.URLField(verbose_name='url')

    def set_url(self, url):
        self.url = url

    def __str__(self):
        return self.target_url


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    urls = models.ManyToManyField(ShortUrl, related_name='urls', blank=True, null=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
