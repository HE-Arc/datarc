# Generated by Django 4.0.2 on 2022-03-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
    ]