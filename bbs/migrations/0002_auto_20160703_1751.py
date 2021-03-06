# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-03 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_userprofile_friends_+', to='bbs.UserProfile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(upload_to='uploads', verbose_name='文章标题图片'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', '草稿'), ('published', '已发布'), ('hidden', '隐藏')], default='published', max_length=32),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='head_img',
            field=models.ImageField(blank=True, height_field=150, null=True, upload_to='', width_field=150),
        ),
    ]
