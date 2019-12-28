#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "版权所有@源码商城：https://shop530346312.taobao.com/?spm=a1z10.1-c.0.0.1c1f6daeeNP5VM"
__date__ = "2019/05/07 17:35"

import xadmin
from xadmin import views

from .models import Info, Categories, Tags, Articles, GetMessage


class BaseSetting:
    """
    开启后台主题功能
    """
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


class GlobalSettings:
    """
    修改后台名称及底部名称
    """
    site_title = '博客后台管理'
    site_footer = '博客后台管理'


class InfoAdmin:
    """
    自定义后台博主信息配置
    """
    # 显示的内容字段，列表顺序即为展示顺序
    list_display = ['name', 'address', 'phone', 'email']
    model_icon = 'fa fa-user'


class CategoriesAdmin:
    model_icon = 'fa fa-bars'


class TagsAdmin:
    model_icon = 'fa fa-tags'


class ArticlesAdmin:
    """
    自定义后台博文配置
    """
    # 显示的内容字段，列表顺序即为展示顺序
    list_display = ['title', 'categorie', 'add_time', 'click_nums', 'comment_nums', 'fav_nums']

    # 过滤字段设置
    list_filter = ['title', 'categorie']

    # 搜索字段设置
    search_fields = ['title', 'categorie']

    # 不可自定义项目
    readonly_fields = ['click_nums', 'comment_nums', 'fav_nums']

    # 配置富文本编辑器
    style_fields = {"content": "ueditor"}
    model_icon = 'fa fa-book'


class GetMessageAdmin:
    model_icon = 'fa fa-envelope-o'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(Info, InfoAdmin)
xadmin.site.register(Categories, CategoriesAdmin)
xadmin.site.register(Tags, TagsAdmin)
xadmin.site.register(Articles, ArticlesAdmin)
xadmin.site.register(GetMessage, GetMessageAdmin)
