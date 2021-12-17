# coding: utf8
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        max_length=500,
        null=True,
        blank=True
    )
    birthday = models.DateField(
        'Дата рождения',
        null=True,
        blank=True
    )
    gender = models.CharField(
        'Гендер',
        max_length=10,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username