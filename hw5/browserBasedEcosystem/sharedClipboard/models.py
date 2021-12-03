# coding: utf8
from django.db import models
from user.models import UserBase


class FileInfo(models.Model):
    name = models.CharField(max_length=32,
                            null=True,
                            verbose_name='Название файла')
    type = models.CharField(max_length=32,
                            null=True,
                            verbose_name='Тип файла')


class FileBase(models.Model):
    path = models.CharField(max_length=64,
                            null=False,
                            verbose_name='Путь к файлу')
    createDataTime = models.DateTimeField(max_length=64,
                                          null=False,
                                          verbose_name='Дата и время создания файла')
    owner = models.ForeignKey(UserBase,
                              null=False,
                              on_delete=models.CASCADE,
                              verbose_name='Владелец файла')
    info = models.OneToOneField(FileInfo,
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name='Необязательная информация о файле')
