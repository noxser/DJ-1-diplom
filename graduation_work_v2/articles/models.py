from django.db import models
from shop.models import Product


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    text = models.TextField(blank=True, verbose_name='Содержание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    active_status = models.BooleanField(default=True, verbose_name='Статус')
    positions = models.PositiveIntegerField(default=0, verbose_name='Позиция на главной')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def display_article_items(self):
        """
        Получаем связанные со статьей товары
        """
        return ArticleItem.objects.filter(article=self.id)

    display_article_items.short_description = 'Связанные товары'


class ArticleItem(models.Model):
    article = models.ForeignKey(Article, related_name='article', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='article_items', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
