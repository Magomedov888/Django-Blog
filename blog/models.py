from audioop import reverse
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse('home')