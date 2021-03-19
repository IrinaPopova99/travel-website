from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class Traveller(AbstractUser):
    country = models.CharField(verbose_name='Страна', max_length=50)
    photo = models.ImageField(verbose_name='Фото', upload_to='users/')
    birthday = models.DateField(verbose_name='Дата рождения')
    about = models.CharField(verbose_name='Описание', max_length=2000)
    countries = models.CharField(verbose_name='Страны', max_length=1000)

    def __str__(self):
        return self.last_name


class Post(models.Model):
    id_traveller = models.ForeignKey(Traveller, on_delete=models.CASCADE)
    country = models.CharField(verbose_name='Страна', max_length=150)
    photo = models.ImageField(verbose_name='Фото', upload_to='posts/')
    data_create = models.DateField(verbose_name='Дата создания', default=datetime.date.today())
    text = models.CharField(verbose_name='Описание', max_length=3000)
    count_likes = models.IntegerField(verbose_name='Количество лайков', default=0)


class Comment(models.Model):
    id_traveller = models.ForeignKey(Traveller, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_create = models.DateField(verbose_name='Дата создания', default=datetime.date.today())
    text = models.CharField(verbose_name='Описание', max_length=1500)
