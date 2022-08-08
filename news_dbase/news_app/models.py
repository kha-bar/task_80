# from django.db import models
from django.urls import reverse

from news_db.models import *


class Post(Post):

    # name = super(Post, self.post_title)

    def __str__(self):
        return f'{self.post_title.title()}: {self.post_text[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Category(Category):

    def __str__(self):
        return self.name_category.title()


class LocalUser(LocalUser):
    pass


# from django.db import models
# from django.core.validators import MinValueValidator
#
#
# # Товар для нашей витрины ???
# class Post(models.Model):
#     name = models.CharField(
#         max_length=50,
#         unique=True, # названия новости не должны повторяться
#     )
#     description = models.TextField()
#     quantity = models.IntegerField(
#         validators=[MinValueValidator(0)],
#     )
#     # поле категории будет ссылаться на модель категории
#     category = models.ForeignKey(
#         to='Category',
#         on_delete=models.CASCADE,
#         related_name='products', # все продукты в категории будут доступны через поле products
#     )
#     price = models.FloatField(
#         validators=[MinValueValidator(0.0)],
#     )
#
#     def __str__(self):
#         return f'{self.name.title()}: {self.description[:20]}'
#
#
# # Категория, к которой будет привязываться новости
# class Category(models.Model):
#     # названия категорий тоже не должны повторяться
#     name = models.CharField(max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name.title()
