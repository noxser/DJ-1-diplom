from django.db import models
import uuid

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    merchandise_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Айди товара')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.category.slug, self.merchandise_id])


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    creator = models.CharField(max_length=200, verbose_name='Автор')
    text = models.TextField(blank=True, verbose_name='Отзыв')
    rating = models.PositiveIntegerField(default=False, verbose_name='Рейтинг')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def stars_rating(self):
        return str(self.rating * '★')
