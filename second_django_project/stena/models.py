from django.db import models

# Create your models here.
from django.db import models


class Mes(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Содержание сообщения')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена (если указана)')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    category = models.ForeignKey('Category', related_name='notes' , null=True, on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']


class Category(models.Model):
    name = models.CharField(max_length=25, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']