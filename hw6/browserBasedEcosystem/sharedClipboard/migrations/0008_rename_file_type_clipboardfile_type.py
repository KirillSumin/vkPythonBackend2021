# Generated by Django 3.2.9 on 2021-12-04 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharedClipboard', '0007_alter_clipboardfile_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clipboardfile',
            old_name='file_type',
            new_name='type',
        ),
    ]
