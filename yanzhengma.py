#!/usr/bin/env python
# coding:utf-8
# Author:Nan ji dong
# 用PIL写一个生成验证码的脚本
# 验证码：为了防止暴力破解

import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Image 负责处理图片
# ImageDraw 负责处理画笔
# ImageFont 负责处理字体
# ImageFilter 负责处理滤镜
# 项目思路：
# 定义一张图片
img = Image.new("RGB", (150, 50), (255, 255, 255))
draw = ImageDraw.Draw(img)
for i in range(random.randint(1, 10)):
    draw.line(
        [
            (random.randint(1, 150), random.randint(1, 150)),
            (random.randint(1, 150), random.randint(1, 150))
        ],
        fill=(0, 0, 0)
    )
    # 绘制点
for i in range(1000):
    draw.point(
        [
            random.randint(1, 150),
            random.randint(1, 150)
        ],
        fill=(0, 0, 0)
    )
font_list = list("abcdefghijklmnopqrstuvmxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
c_chars = "".join(random.sample(font_list, 5))

font = ImageFont.truetype("simsun.ttc", 32)
draw.text((5, 5), c_chars, font=font, fill="green")

params = [1 - float(random.randint(1, 2)) / 100,
          0,
          0,
          0,
          1 - float(random.randint(1, 2)) / 100,
          float(random.randint(1, 2)) / 500,
          0.001,
          float(random.randint(1, 1)) / 500,
          ]

img = img.transform((150, 50), Image.PERSPECTIVE, params)
img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
img.show()
