# Generated by Django 3.2.9 on 2021-12-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharedClipboard', '0004_alter_clipboardfile_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clipboardfile',
            name='create_data_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания файла'),
        ),
    ]