#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "版权所有@源码商城：https://shop530346312.taobao.com/?spm=a1z10.1-c.0.0.1c1f6daeeNP5VM"
__date__ = "2019/05/10 11:45"

# form表单验证

from django import forms
from .models import GetMessage


class GetMessageForm(forms.ModelForm):
    """读者留言验证,注意这里继承的是ModelForm"""

    class Meta:
        """继承GetMessage类"""
        model = GetMessage
        fields = ['name', 'email', 'subject', 'message']
