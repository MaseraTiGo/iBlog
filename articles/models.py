#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "版权所有@源码商城：https://shop530346312.taobao.com/?spm=a1z10.1-c.0.0.1c1f6daeeNP5VM"
__date__ = "2019/04/12 14:46"

# 常规模块的引入分为三部分，依次为：
# Python内置模块（如json、datetime）、第三方模块（如Django）、自己写的模块

from datetime import datetime  # 内置的日期时间模块
from django.db import models  # 创建Django模型
from DjangoUeditor.models import UEditorField  # 富文本编辑器


class Info(models.Model):
    """博主信息管理"""
    name = models.CharField(verbose_name='显示名称', max_length=10)  # 定义显示名称字段，当前设置可在数据库相应的表中创建一个name字段，字符类型，长度为10
    address = models.CharField(verbose_name='地址', max_length=100)
    phone = models.CharField(verbose_name='电话', max_length=20)
    email = models.EmailField(verbose_name='邮箱')

    class Meta:  # 元类，可定义该模块的基本信息
        verbose_name = '博主信息'
        verbose_name_plural = verbose_name

    def __str__(self):  # 当print输出实例对象，或str() 实例对象时，调用这个方法
        return self.name


class Categories(models.Model):
    """博文分类管理，同博文是一对多的关系"""

    name = models.CharField(verbose_name='名称', max_length=20)

    class Meta:
        verbose_name = '博文分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tags(models.Model):
    """标签管理，同博文是多对多的关系"""
    name = models.CharField(verbose_name='名称', max_length=20)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Articles(models.Model):
    """博文管理"""
    title = models.CharField(verbose_name='标题', max_length=20)
    img = models.ImageField(verbose_name='封面图', upload_to='articles', blank=True, null=True)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False, verbose_name='所属类别')
    tags = models.ManyToManyField(Tags)
    # datetime.now不可加()
    add_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    click_nums = models.IntegerField(verbose_name='阅读数', default=0)
    comment_nums = models.IntegerField(verbose_name='评论数', default=0)
    fav_nums = models.IntegerField(verbose_name='点赞数', default=0)
    info = models.CharField(verbose_name='摘要', max_length=200, default='', blank=True)
    # 富文本编辑器配置
    content = UEditorField(verbose_name='博文内容',
                           width=700,
                           height=400,
                           toolbars='full',
                           imagePath='articles/',
                           filePath='articles/',
                           upload_settings={'imageMaxSizing': 1024000},
                           default='')
    is_index = models.BooleanField(verbose_name='是否首页轮播', default=0)
    belong_to = models.ForeignKey(Info,null=False,default=1,on_delete=models.CASCADE)
    def viewed(self):
        """
        增加阅读数
        """
        self.click_nums += 1
        self.save(update_fields=['click_nums'])

    def addfav(self):
        """
        增加评论数
        """
        self.fav_nums += 1
        self.save(update_fields=['fav_nums'])

    class Meta:
        verbose_name = '博文'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GetMessage(models.Model):
    """留言信息管理"""
    name = models.CharField(verbose_name='姓名', max_length=20)
    email = models.EmailField(verbose_name='邮箱')
    subject = models.CharField(verbose_name='主题', max_length=100)
    message = models.TextField(verbose_name='内容')

    class Meta:
        verbose_name = "留言处理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
