# Generated by Django 3.2.9 on 2021-12-04 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharedClipboard', '0002_auto_20211204_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clipboardfile',
            name='name',
        ),
    ]
