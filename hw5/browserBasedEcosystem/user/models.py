# coding: utf8
from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=32,
                            null=True,
                            verbose_name='Имя пользователя')
    gender = models.CharField(max_length=10,
                              null=True,
                              verbose_name='Пол пользователя')
    about = models.CharField(max_length=128,
                             null=True,
                             verbose_name='Произвольное описание пользователя')


class UserBase(models.Model):
    info = models.OneToOneField(UserInfo,
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name='Необязательное информация о пользователе')
