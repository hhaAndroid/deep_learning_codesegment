import numpy as np
from library.c4_bbox_iou import bbox_overlaps


def demo_bbox_iou():
    pred_bbox3 = np.array([[10, 20, 60, 65, 0.6],
                           [10, 27, 60, 75, 0.8],
                           [50, 90, 90, 95, 0.45],
                           [10, 90, 90, 95, 0.8],
                           [20, 60, 30, 75, 0.1]])  # xyxy
    gt_bbox3 = np.array([[10, 20, 60, 60],
                         [50, 70, 90, 95]]).reshape(-1, 4)  # xyxy

    iou = bbox_overlaps(pred_bbox3[:, :4], gt_bbox3)
    print(iou)


if __name__ == '__main__':
    demo_bbox_iou()
