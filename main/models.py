# Create your models here.

from django.db import models


#Task
class Task(models.Model):
    title = models.CharField('Имя', max_length=100)
    task = models.TextField('Отзыв')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'


#Catalogue
class Catalogue(models.Model):
    title = models.CharField(max_length=100)
    # url = models.URLField('url', max_length=500, blank=True, null=True, default=None)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукты'




# Products
# class Products(models.Model):
#     TEST = 'test'
#     DEV = 'dev'

#     OPTIONS = (
#         ('test', TEST),
#         ('dev', DEV)
#     )

#     title = models.CharField(max_length=30)
#     url = models.URLField('url', max_length=500, blank=True, null=True, default=None)
#     price = models.IntegerField(blank=True, null=True)
#     type = models.CharField(max_length=10, choices=OPTIONS, default=TEST, blank=True, null=True)

#     def __str__(self):
#         return f'{self.title} - {self.price}'