# -*- coding:utf-8 -*-
# deep eyes.

import torch


# from MMClassification
def acc_topk_torch(pred, target, topk=1):
    assert isinstance(topk, (int, tuple))
    if isinstance(topk, int):
        topk = (topk,)
        return_single = True
    else:
        return_single = False

    maxk = max(topk)
    _, pred_label = pred.topk(maxk, dim=1)
    pred_label = pred_label.t()
    correct = pred_label.eq(target.view(1, -1).expand_as(pred_label))

    res = []
    for k in topk:
        correct_k = correct[:k].view(-1).float().sum(0, keepdim=True)
        res.append(correct_k.mul_(100.0 / pred.size(0)))
    return res[0] if return_single else res


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
