# deep_learning_codesegment
Code segment are often used in deep learning algorithms(pytorch/numpy)

本仓库主要是收集在深度学习算法开发中经常用到的函数，有以下几个目的：

1. 抽查成单独的函数，方便理解代码
2. 方便日后调用，相当于工具类
3. 学习目的，掌握pytorch/numpy的常用和高级用法
4. 面试常常问到这些基础内容



本仓库会不断新增函数，新增的内容主要是

(1) 非常常用且通用操作；

(2) 涉及到pytorch/numpy的高级用法，出于学习目的



注意：本仓库代码不一定是本人写的，可能来自很多库，我主要是借鉴和学习，每个借鉴代码都会注释来做何处。每个新增函数都会进行测试，再上传，保证质量。

**每个函数或者类都有对应的测试代码，在tools文件夹下**

## 摘要

[detail](docs/detail.md)   

### 1 acc_topk

​	分类任务中经常需要计算topk acc指标，本函数支持输入list来计算得到任意topk的acc指标

### 2 img_show

​    opencv写的图片显示功能，支持单张图、多张图、多张图合并、多张图自定义行列数显示功能；支持bbox显示；支持中文显示

### 3 pr_roc

​    二分类问题绘制pr和roc曲线，以及auc指标

### 4 bbox_iou

   两组bbox的iou计算函数，目前仅仅包括正矩形bbox iou计算，后面会包括倾斜框iou计算

### 5 voc_map

   支持voc2007和voc2012两组mAP评估指标计算
   
### 6 python_trick

   收集开发中常用的python稍微高级点的trick,
1. 如何将dict参数自动变成类内部属性？
2. 如何将字典变成可以属性访问?


### 7 numpy_trick

   收集开发中常用的numpy稍微高级点的trick

### 8 torch_trick

   收集开发中常用的torch稍微高级点的trick
