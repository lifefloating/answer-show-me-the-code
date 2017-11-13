#!/usr/bin/env python3.5
# encoding: utf-8
# author: yqq

import os
from PIL import Image

pathDir = 'C:/workspace'
os.chdir(pathDir)


def modify_imgsize():
    for filename in get_imglist():
        img = Image.open(filename)
        if max(img.size) > 1136:
            value = max(img.size) / 1136.0
            newsize_min = min(img.size) / value
            newimg = img.resize((1136, int(newsize_min)), Image.ANTIALIAS)  # 修改大小
            newimg.save('new_' + filename)
        else:
            print("This picture is availabe:" + filename)


def get_imglist():  # 获取照片名称list
    img_list = []
    list_dir = os.listdir(pathDir)
    for x in list_dir:
        if '.jpg' in x:
            img_list.append(x)
        else:
            print("This is not a picture: " + x)
    return img_list


modify_imgsize()