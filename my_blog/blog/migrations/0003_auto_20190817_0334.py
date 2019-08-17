# Generated by Django 2.1 on 2019-08-17 03:34

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190817_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='video',
            field=models.FileField(default='blog/article/icon/ckin.mp4', upload_to=blog.models.user_avatar_path, verbose_name='视频'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='picture',
            field=models.ImageField(default='blog/article/icon/20190817_031833.jpg', upload_to=blog.models.user_avatar_path, verbose_name='缩略图'),
        ),
    ]
