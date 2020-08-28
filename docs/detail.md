# 详情

## 1 acc_topk

[c1_acc_topk](../library/c1_acc_topk.py)   

分类任务中经常需要计算topk acc指标，本函数支持输入list来计算得到任意topk的acc指标

## 2 img_show

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

支持中文

```python
img = ImageHelper.cv2ImgAddText(img, '这是一个测试中文代码', 10, 10, textSize=8, font='./NotoSansCJK-Bold')
```

需要注意的是需要字体库支持，我采用的是NotoSansCJK-Bold，后缀是.ttc，ubuntu系统下有，可以查找出来。



## 3 pr_roc

[c3_pr_roc](../library/c3_pr_roc.py) 

​    分类问题中，对于类别不平衡问题，采用acc指标是不够的，pr曲线和roc曲线绘制来评估模型性能比较关键。

核心内容可以参考知乎文章：https://zhuanlan.zhihu.com/p/34655990 ，我简单写了下，链接为 https://www.zybuluo.com/huanghaian/note/1736925

   使用示例请见tools目录下的对应文件

## 4 bbox_iou

[c4_bbox_iou](../library/c4_bbox_iou.py) 

   两组bbox的iou计算函数，目前仅仅包括正矩形bbox iou计算，后面会包括倾斜框iou计算

```python
pred_bbox3 = np.array([[10, 20, 60, 65, 0.6],
                           [10, 27, 60, 75, 0.8],
                           [50, 90, 90, 95, 0.45],
                           [10, 90, 90, 95, 0.8],
                           [20, 60, 30, 75, 0.1]])  # xyxy
gt_bbox3 = np.array([[10, 20, 60, 60],
                         [50, 70, 90, 95]]).reshape(-1, 4)  # xyxy

iou = bbox_overlaps(pred_bbox3[:, :4], gt_bbox3)
print(iou)
```



## 5 voc_map

[c5_voc_mAP](../library/c5_voc_mAP.py) 

   支持voc2007和voc2012两组mAP评估指标计算 ,需要注意的是本函数实现的mAP指标，并没有考虑面积过小的预测框不算以及gt bbox要忽略的部分。

   本函数主要是出于学习目的写的，基本上都有注释，如果想知道mAP原理，可以参考链接  https://www.zybuluo.com/huanghaian/note/1736925， 我进行了简单说明

   重点摘要：

1. VOC2007的AP计算方法是所谓的11点法即选取Recall >= 0, 0.1, ..., 1的11处Percision的最大值，计算AP=11点处的精度最大值和/11
2. VOC2012的评估指标就是标准的PR曲线下面积，原理请参考c3

  使用示例请见tools目录下的对应文件


## 6 python_trick
[c6_python_trick](../library/c6_python_trick.py)    

   收集开发中常用的python稍微高级点的trick
1. 如何将dict参数自动变成类内部属性？
通过self.__ dict __.update实现
2. 如何将字典变成可以属性访问?
有两种方式：可以直接用第三方库addict实现；也可以自己简化写，核心就是递归+__ getattr __方法
3. 复杂dict如何打印的漂亮，更有层次感？
借助yapf库实现的pep8自动格式化字符串即可，我们要做的仅仅需要把dict按照行排列切割好就行，后面的每行如何格式化采用pep8标准自动执行


## 7 numpy_trick

[c7_numpy_trick](../library/c7_numpy_trick.py)    
   收集开发中常用的numpy稍微高级点的trick

## 8 torch_trick

[c8_torch_trick](../library/c8_torch_trick.py)    
   收集开发中常用的torch稍微高级点的trick