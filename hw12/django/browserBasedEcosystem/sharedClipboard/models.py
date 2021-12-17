# coding: utf8
from django.db import models
from django.contrib.auth import get_user_model
import os

User = get_user_model()


class ClipboardFile(models.Model):
    path = models.CharField(max_length = 200, verbose_name='Путь до файла относительно BASE_PATH', unique=True)

    create_data_time = models.DateTimeField('Дата и время создания файла',
                                            auto_now_add=True, blank=True)
    owner = models.ForeignKey(User,
                              null=False,
                              on_delete=models.CASCADE,
                              verbose_name='Владелец файла')

    type = models.CharField(max_length=32,
                                 null=True,
                                 verbose_name='Тип файла',
                                 blank=True)

    class Meta:
        verbose_name = 'Файл б/о'
        verbose_name_plural = 'Файлы б/о'

    def __str__(self):
        return self.path
