# 详情

## 1 acc_topk

[c1_acc_topk](../library/c1_acc_topk.py)   

分类任务中经常需要计算topk acc指标，本函数支持输入list来计算得到任意topk的acc指标

## 2. img_show

[c2_img_show](../library/c2_img_show.py)   

​    opencv写的图片显示功能，支持单张图、多张图、多张图合并、多张图自定义行列数显示功能;支持bbox显示

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

   bbox可以是list或者numpy格式输入

```python
# 如果不指定颜色，则采用随机颜色
ImageHelper.show_bbox(img, bbox_list, font_scale=0.2, thickness=1)
# 如果指定，则采用给定颜色，支持图片数据返回
ImageHelper.show_bbox(img, bbox_list, color=(255, 0, 0), font_scale=0.2, thickness=1)
# is_without_mask表示bbox内部会显示mask
ImageHelper.show_bbox(img, bbox_list, color=(255, 0, 0), font_scale=0.2, thickness=1,is_without_mask=True)
```

## 3 pr_roc
[c3_pr_roc](../library/c3_pr_roc.py) 

​    分类问题中，对于类别不平衡问题，采用acc指标是不够的，pr曲线和roc曲线绘制来评估模型性能比较关键。

核心内容可以参考知乎文章：https://zhuanlan.zhihu.com/p/34655990 ，我简单写了下，链接为 https://www.zybuluo.com/huanghaian/note/1736925

   

