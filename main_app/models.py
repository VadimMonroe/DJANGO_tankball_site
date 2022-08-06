from django.db import models

# Create your models here.

class Messages(models.Model):
    form_name = models.CharField('Имя', max_length=50)
    message = models.CharField('Сообщение', max_length=1000)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.form_name

    class Meta:
        verbose_name = 'Сообщениe в Форме'
        verbose_name_plural = 'Сообщения в Форме'