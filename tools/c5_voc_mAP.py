# -*- coding:utf-8 -*-
# deep eyes
import numpy as np
from library.c5_voc_mAP import voc_eval_map


def demo_voc2007_map():
    # 先构造仿真数据
    # 单类分析,多类别也是一样，追加list就行

    # 第一张图片，模拟漏报
    gt_bbox1 = np.array([10, 20, 40, 60]).reshape(-1, 4)  # xyxy
    pred_bbox1 = np.array([]).reshape((0, 5))  # 即使是空，也必须有shape，否则代码会报错

    # 第二张图片，模拟误报
    gt_bbox2 = np.array([10, 20, 60, 60]).reshape(-1, 4)  # xyxy
    pred_bbox2 = np.array([[10, 17, 60, 65, 0.9],
                           [10, 27, 60, 75, 0.8],
                           [5, 17, 60, 85, 0.45]])

    # 第三张图片，模拟混合
    gt_bbox3 = np.array([[10, 20, 60, 60],
                         [50, 70, 90, 95]]).reshape(-1, 4)  # xyxy

    pred_bbox3 = np.array([[10, 20, 60, 65, 0.6],
                           [10, 27, 60, 75, 0.8],
                           [50, 90, 90, 95, 0.45],
                           [10, 90, 90, 95, 0.8],
                           [20, 60, 30, 75, 0.1]])

    results = [[pred_bbox1], [pred_bbox2], [pred_bbox3]]
    annotations = [[gt_bbox1], [gt_bbox2], [gt_bbox3]]
    voc2007_map = voc_eval_map(results, annotations, name='voc2007')
    voc2012_map = voc_eval_map(results, annotations, name='voc2012')
    print('voc2007_map=', voc2007_map, 'voc2012_map=', voc2012_map)


if __name__ == '__main__':
    demo_voc2007_map()
