# -*- coding:utf-8 -*-
# deep eyes.

import numpy as np
import cv2
from library.c2_img_show import ImageHelper


def demo_img_show():
    # 创建5张假图片
    input_shape = [100, 100, 3]
    img = np.zeros(input_shape, np.uint8)
    cv2.rectangle(img, (20, 20), (60, 60), (255, 255, 255))
    # ImageHelper.show_img(img)  # 显示单张图片,默认名称显示
    ImageHelper.show_img(img, 'img')  # 给定窗口名

    img2 = img.copy()
    cv2.rectangle(img2, (30, 20), (50, 60), (255, 255, 0))
    img3 = img2.copy()
    cv2.rectangle(img3, (33, 28), (50, 90), (255, 0, 0))
    img4 = img3.copy()
    cv2.rectangle(img4, (33, 28), (90, 97), (255, 0, 255))
    img5 = img4.copy()
    cv2.rectangle(img5, (93, 28), (100, 97), (0, 0, 255))
    # ImageHelper.show_img([img, img2, img3, img4, img5])  # 分离显示，默认名称
    # ImageHelper.show_img([img, img2, img3, img4, img5], ['img', 'img2', 'img3', 'img4', 'img5'])  # 分离显示，指定名称
    # ImageHelper.show_img([img, img2, img3, img4, img5], is_merge=True)  # 合并显示,默认单行
    # ImageHelper.show_img([img, img2, img3, img4, img5], is_merge=True, row_col_num=(-1, 1))  # 合并显示,单列
    ImageHelper.show_img([img, img2, img3, img4, img5], is_merge=True, row_col_num=(2, 3))  # 合并显示，指定数目


if __name__ == '__main__':
    demo_img_show()