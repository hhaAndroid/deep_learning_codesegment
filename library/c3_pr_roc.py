# -*- coding:utf-8 -*-
# deep eyes
import numpy as np


# https://zhuanlan.zhihu.com/p/34655990
def calc_PR_curve(pred, label):
    threshold = np.sort(pred)[::-1]  # pred是每个样本的正例预测概率值,逆序
    label = label[pred.argsort()[::-1]]
    precision = []
    recall = []
    tp = 0
    fp = 0
    ap = 0  # 平均精度
    for i in range(len(threshold)):
        if label[i] == 1:
            tp += 1
            recall.append(tp / len(label))
            precision.append(tp / (tp + fp))
            ap += (recall[i] - recall[i - 1]) * precision[i]  # 近似曲线下面积
        else:
            fp += 1
            recall.append(tp / len(label))
            precision.append(tp / (tp + fp))

    return precision, recall, ap


def calc_ROC_curve(pred, label):
    pos = label[label == 1]
    neg = label[label == 0]
    threshold = np.sort(pred)[::-1]  # pred是每个样本的正例预测概率值,逆序
    label = label[pred.argsort()[::-1]]
    tpr_all = [0]
    fpr_all = [0]
    tpr = 0
    fpr = 0
    x_step = 1 / float(len(neg))
    y_step = 1 / float(len(pos))
    y_sum = 0
    for i in range(len(threshold)):
        if label[i] == 1:
            tpr += y_step
            tpr_all.append(tpr)
            fpr_all.append(fpr)
        else:
            fpr += x_step
            fpr_all.append(fpr)
            tpr_all.append(tpr)
            y_sum += tpr
    return tpr_all, fpr_all, y_sum*x_step
