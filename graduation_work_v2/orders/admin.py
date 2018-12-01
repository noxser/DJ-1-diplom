from django.contrib import admin

from .models import Order, OrderItem


# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    """
    Дополнительные поля можно получить как в админке,
    так и из модели обратившись, плюс обращения из модели можно
    добавить русское название
    """
    # поля отображаемые при открытии списка заказов
    list_display = ['user',
                    'user_email',
                    'created',
                    'display_num_orders',
                    'fulfilled',
                    ]
    list_editable = ['fulfilled']
    list_filter = ['id', 'created']
    # поля отображаемые при открытии конкретого заказа
    fields = ('user',
              'first_name',
              'last_name',
              'user_email',
              'fulfilled',
              )
    readonly_fields = ('user_email',
                       'first_name',
                       'last_name'
                       )

    def email_from_admin(self, obj):
        return obj.user.email

    def first_name(self, obj):
        if obj.user.first_name:
            return obj.user.first_name
        else:
            return 'не указано'

    def last_name(self, obj):
        if obj.user.last_name:
            return obj.user.last_name
        else:
            return 'не указано'

    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
