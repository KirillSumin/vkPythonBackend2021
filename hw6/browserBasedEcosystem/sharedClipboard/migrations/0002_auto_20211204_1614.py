# Generated by Django 3.2.9 on 2021-12-04 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharedClipboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clipboardfile',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец файла'),
        ),
        migrations.AlterField(
            model_name='clipboardfile',
            name='path',
            field=models.FilePathField(path='userFiles', unique=True, verbose_name='Путь до файла'),
        ),
    ]
