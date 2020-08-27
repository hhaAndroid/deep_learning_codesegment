# 详情

## 1 acc_topk

[c1_acc_topk](../library/c1_acc_topk.py)   

分类任务中经常需要计算topk acc指标，本函数支持输入list来计算得到任意topk的acc指标

## 2. img_show

[c2_img_show](../library/c2_img_show.py)   

​    opencv写的图片显示功能，支持单张图、多张图、多张图合并、多张图自定义行列数显示功能

使用示例：

```python
ImageHelper.show_img(img)  # 显示单张图片,默认名称显示
ImageHelper.show_img(img, 'img')  # 给定窗口名
ImageHelper.show_img([img, img2, img3, img4, img5])  # 分离显示，默认名称
ImageHelper.show_img([img, img2, img3, img4, img5], ['img', 'img2', 'img3', 'img4', 'img5'])  # 分离显示，指定名称
ImageHelper.show_img([img, img2, img3, img4, img5], is_merge=True)  # 合并显示,默认单行
ImageHelper.show_img([img, img2, img3, img4, img5], is_merge=True, row_col_num=(-1, 1))  # 合并显示,单列
ImageHelper.show_img([img, img2, img3, img4, img5], is_merge=True, row_col_num=(2, 3))  # 合并显示，指定数目
ImageHelper.show_img([img, img2, img3, img4, img5], is_merge=True, row_col_num=(2, -1))  # 合并显示，指定数目
```

