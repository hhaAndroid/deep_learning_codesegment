# -*- coding:utf-8 -*-
# deep eyes.

import torch
import matplotlib.pyplot as plt
from library.c1_acc_topk import acc_topk_torch
from library.c3_pr_roc import calc_PR_curve, calc_ROC_curve


def get_data():
    pred = [[0.1, 0.2],
            [0.1, 0.6],
            [0.2, 0.3],
            [0.9, 0.3],
            [0.9, 0.3],
            [0.14, 0.2],
            [0.11, 0.25],
            [0.2, 0.3],
            [0.1, 0.5],
            [0.1, 0.3],
            [0.23, 0.65],
            [0.2, 0.63],
            [0.2, 0.63],
            [0.19, 0.3],
            ]
    label = [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0]
    pred = torch.tensor(pred).float()
    pred = torch.softmax(pred, dim=1)
    label = torch.tensor(label).long()
    return pred, label


def demo_pr():
    pred, label = get_data()
    top1 = acc_topk_torch(pred, label)
    print(top1)

    positive = pred.numpy()[:, 0]
    target = label.numpy()

    # sklearn自带pr曲线
    # from sklearn import metrics
    # precision, recall, _ = metrics.precision_recall_curve(target, positive)
    # plt.plot(recall, precision)
    # plt.xlabel('recall')
    # plt.ylabel('precision')
    # plt.show()

    precision, recall, ap = calc_PR_curve(positive, target)
    print(ap)
    plt.plot(recall, precision)
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.show()


def demo_roc():
    pred, label = get_data()

    positive = pred.numpy()[:, 0]
    target = label.numpy()

    # # sklearn自带pr曲线
    from sklearn import metrics
    # fpr, tpr, _ = metrics.roc_curve(target, positive)
    # auc = metrics.auc(fpr, tpr)
    # print(auc)
    # plt.plot(fpr, tpr)
    # plt.xlabel('False Positive Rate')
    # plt.ylabel('True Positive Rate')
    # plt.show()

    tpr_all, fpr_all, auc = calc_ROC_curve(positive, target)
    print(auc)
    plt.plot(fpr_all, tpr_all)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.show()


if __name__ == '__main__':
    demo_pr()
    demo_roc()
