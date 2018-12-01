from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    fulfilled = models.BooleanField(default=False, verbose_name='Статус')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def display_num_orders(self):
        """
        Кол-во товаров
        """
        return OrderItem.objects.filter(order=self.id).count()

    display_num_orders.short_description = 'Количество товаров'

    def user_email(self):
        """
        Электронная почта
        """
        return self.user.email

    user_email.short_description = 'Email пользователя'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Колличество')
