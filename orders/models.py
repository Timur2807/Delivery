from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Orders(models.Model):
    PACKAGE = [
        ('Letter', 'Письмо'),
        ('Parcel', 'Бандероль',),
        ('Overall cargo', 'Габаритный груз',)
    ]
    ORDER_STATUS = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Handed to courier', 'Handed to courier'),
        ('Done', 'Done'),
        ('Cancelled', 'Cancelled')
    ]
    city = models.CharField('Город', max_length=150, blank=True)
    address = models.TextField('Адрес', max_length=300, blank=True)
    date_delivery = models.DateField('Дата доставки', blank=True)
    time_delivery = models.TimeField('Время доставки', blank=True)
    customer = models.CharField('Заказчики', max_length=150, blank=True)
    comment = models.TextField('Комментарий', max_length=200, blank=True, null=True)
    package = models.CharField('Тип посылки', max_length=20, choices=PACKAGE, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status_order = models.CharField('Статус посылки', max_length=25, choices=ORDER_STATUS, blank=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
