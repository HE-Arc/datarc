# Generated by Django 4.0.2 on 2022-03-16 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_file_useraccess_userfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='url',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
