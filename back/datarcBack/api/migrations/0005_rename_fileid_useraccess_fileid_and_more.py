# Generated by Django 4.0.2 on 2022-03-16 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_file_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccess',
            old_name='FileId',
            new_name='fileId',
        ),
        migrations.RenameField(
            model_name='useraccess',
            old_name='UserId',
            new_name='userId',
        ),
        migrations.RenameField(
            model_name='userfile',
            old_name='FileId',
            new_name='fileId',
        ),
        migrations.RenameField(
            model_name='userfile',
            old_name='UserId',
            new_name='userId',
        ),
    ]