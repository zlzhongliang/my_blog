# Generated by Django 2.1 on 2019-08-24 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190823_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
    ]
