from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Messages(models.Model):
    form_name = models.CharField('Имя', max_length=50)
    message = models.CharField('Сообщение', max_length=1000)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.form_name

    def get_absolute_url(self):
        return f'/form-comments/{self.id}'

    class Meta:
        verbose_name = 'Сообщениe в Форме'
        verbose_name_plural = 'Сообщения в Форме'
        db_table = 'MessagesForm'


class Category(models.Model):
    name = models.CharField('Имя', max_length=50, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщениe в Форме'
        verbose_name_plural = 'Сообщения в Форме'
        db_table = 'MessagesForm2'
