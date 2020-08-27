# -*- coding:utf-8 -*-
# deep eyes.

import torch
from library.c1_acc_topk import acc_topk_torch


def demo_acc_topk_torch():
    num_class = 8
    batch = 4

    pred = torch.rand((batch, num_class)).float()
    pred = torch.softmax(pred, dim=1)
    print('pred=', pred)
    target = torch.randint(num_class, size=(batch,))
    print('target=', target)

    topk = 1
    res = acc_topk_torch(pred, target, topk)
    print('top1=', res.item())

    topk = 5
    res = acc_topk_torch(pred, target, topk)
    print('top5=', res.item())

    topk = (1, 5)
    res = acc_topk_torch(pred, target, topk)
    print('top1=', res[0].item(), 'top5=', res[1].item())


if __name__ == '__main__':
    demo_acc_topk_torch()
