# -*- coding:utf-8 -*-
# deep eyes.
import math
import os
import cv2
import numpy as np

CV2_INTER_DICT = {
    'nearest': cv2.INTER_NEAREST,
    'linear': cv2.INTER_LINEAR,
    'cubic': cv2.INTER_CUBIC
}

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]

# fmt: off
# RGB:
_COLORS = np.array(
    [
        0.000, 0.447, 0.741,
        0.850, 0.325, 0.098,
        0.929, 0.694, 0.125,
        0.494, 0.184, 0.556,
        0.466, 0.674, 0.188,
        0.301, 0.745, 0.933,
        0.635, 0.078, 0.184,
        0.300, 0.300, 0.300,
        0.600, 0.600, 0.600,
        1.000, 0.000, 0.000,
        1.000, 0.500, 0.000,
        0.749, 0.749, 0.000,
        0.000, 1.000, 0.000,
        0.000, 0.000, 1.000,
        0.667, 0.000, 1.000,
        0.333, 0.333, 0.000,
        0.333, 0.667, 0.000,
        0.333, 1.000, 0.000,
        0.667, 0.333, 0.000,
        0.667, 0.667, 0.000,
        0.667, 1.000, 0.000,
        1.000, 0.333, 0.000,
        1.000, 0.667, 0.000,
        1.000, 1.000, 0.000,
        0.000, 0.333, 0.500,
        0.000, 0.667, 0.500,
        0.000, 1.000, 0.500,
        0.333, 0.000, 0.500,
        0.333, 0.333, 0.500,
        0.333, 0.667, 0.500,
        0.333, 1.000, 0.500,
        0.667, 0.000, 0.500,
        0.667, 0.333, 0.500,
        0.667, 0.667, 0.500,
        0.667, 1.000, 0.500,
        1.000, 0.000, 0.500,
        1.000, 0.333, 0.500,
        1.000, 0.667, 0.500,
        1.000, 1.000, 0.500,
        0.000, 0.333, 1.000,
        0.000, 0.667, 1.000,
        0.000, 1.000, 1.000,
        0.333, 0.000, 1.000,
        0.333, 0.333, 1.000,
        0.333, 0.667, 1.000,
        0.333, 1.000, 1.000,
        0.667, 0.000, 1.000,
        0.667, 0.333, 1.000,
        0.667, 0.667, 1.000,
        0.667, 1.000, 1.000,
        1.000, 0.000, 1.000,
        1.000, 0.333, 1.000,
        1.000, 0.667, 1.000,
        0.333, 0.000, 0.000,
        0.500, 0.000, 0.000,
        0.667, 0.000, 0.000,
        0.833, 0.000, 0.000,
        1.000, 0.000, 0.000,
        0.000, 0.167, 0.000,
        0.000, 0.333, 0.000,
        0.000, 0.500, 0.000,
        0.000, 0.667, 0.000,
        0.000, 0.833, 0.000,
        0.000, 1.000, 0.000,
        0.000, 0.000, 0.167,
        0.000, 0.000, 0.333,
        0.000, 0.000, 0.500,
        0.000, 0.000, 0.667,
        0.000, 0.000, 0.833,
        0.000, 0.000, 1.000,
        0.000, 0.000, 0.000,
        0.143, 0.143, 0.143,
        0.857, 0.857, 0.857,
        1.000, 1.000, 1.000
    ]
).astype(np.float32).reshape(-1, 3)


def random_color(rgb=False, maximum=255):
    """
    Args:
        rgb (bool): whether to return RGB colors or BGR colors.
        maximum (int): either 255 or 1

    Returns:
        ndarray: a vector of 3 numbers
    """
    idx = np.random.randint(0, len(_COLORS))
    ret = _COLORS[idx] * maximum
    if not rgb:
        ret = ret[::-1]
    return ret


class ImageHelper(object):
    """
    Provide some basic and significant operations of image
    """

    @staticmethod
    def read_img(img_path, mode='BGR', show_error=True):
        """
        Loads an image from a file. Additionally, opencv loads an image data as 'BGR',
        this function supports three image data modes, 'BGR', 'RGB' and 'GRAY'.
        You can specified loading type through parameter 'mode'.

        :param img_path: string: name of file to be loaded.
        :param mode: string: which data type is wanted.
        :param show_error: bool, is show error info
        :return: img: numpy.ndarray or None
        """
        if not os.path.exists(img_path):
            if show_error: print('img path do not exists!')
            return None
        mode = mode.upper()
        img_bgr = cv2.imread(img_path, cv2.IMREAD_COLOR)
        if img_bgr is None:
            if show_error: print('the img is damaged!')
            return None
        if mode == 'RGB':
            return ImageHelper.convert_bgr_to_rgb(img_bgr)
        elif mode == 'BGR':
            return img_bgr
        elif mode == 'GRAY':
            return ImageHelper.convert_bgr_to_gray(img_bgr)
        else:
            raise NotImplementedError('Not support ' + mode)

    @staticmethod
    def convert_bgr_to_rgb(img_bgr):
        """
        Converts an image from bgr space to rgb space.

        :param img_bgr:numpy.ndarray
        :return img_rgb:numpy.ndarray
        """
        assert isinstance(img_bgr, np.ndarray)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        return img_rgb

    @staticmethod
    def convert_rgb_to_bgr(img_rgb):
        """
        Converts an image from rgb space to bgr space.

        :param img_rgb:numpy.ndarray
        :return img_bgr:numpy.ndarray
        """
        assert isinstance(img_rgb, np.ndarray)
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
        return img_bgr

    @staticmethod
    def convert_bgr_to_gray(img, keep_dim=False):
        """
        Converts an image from bgr space to gray space.
        Optional parameter 'keep_dim' controls channel of return image.

        :param img: numpy.ndarray: bgr space.
        :param keep_dim: if True, return img has same channel as input img, else, channel will reduce 1.

        """
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if keep_dim:
            gray_img = gray_img[..., None]
        return gray_img

    @staticmethod
    def convert_gray_to_bgr(img):
        """
        Converts an image from gray space to bgr space.

        :param img:numpy.ndarray
        :return bgr_img: numpy.ndarray
        """
        if img.ndim == 2:
            img = img[..., None]
        bgr_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        return bgr_img

    @staticmethod
    def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20, font='./NotoSansCJK-Bold.ttc'):
        from PIL import Image, ImageDraw, ImageFont
        if isinstance(img, np.ndarray):  # 判断是否OpenCV图片类型
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img)
        fontText = ImageFont.truetype(font, textSize, encoding="utf-8")
        draw.text((left, top), text, textColor, font=fontText)
        return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

    @staticmethod
    def show_img(imgs, window_names=None, wait_time_ms=0, is_merge=False, row_col_num=(1, -1)):
        """
        Displays an image or a list of images in specified windows or self-initiated windows.
        You can also control display wait time by parameter 'wait_time_ms'.
        Additionally, this function provides an optional parameter 'is_merge' to
        decide whether to display all imgs in a particular window 'merge'.
        Besides, parameter 'row_col_num' supports user specified merge format.
        Notice, specified format must be greater than or equal to imgs number.

        :param imgs: numpy.ndarray or list.
        :param window_names: specified or None, if None, function will create different windows as '1', '2'.
        :param wait_time_ms: display wait time.
        :param is_merge: whether to merge all images.
        :param row_col_num: merge format. default is (1, -1), image will line up to show.
                            example=(2, 5), images will display in two rows and five columns.
        """
        if not isinstance(imgs, list):
            imgs = [imgs]

        if window_names is None:
            window_names = list(range(len(imgs)))
        else:
            if not isinstance(window_names, list):
                window_names = [window_names]
            assert len(imgs) == len(window_names), 'window names does not match images!'

        if is_merge:
            merge_imgs = ImageHelper.merge_imgs(imgs, row_col_num)

            cv2.namedWindow('merge', 0)
            cv2.imshow('merge', merge_imgs)
        else:
            for img, win_name in zip(imgs, window_names):
                if img is None:
                    continue
                win_name = str(win_name)
                cv2.namedWindow(win_name, 0)
                cv2.imshow(win_name, img)

        cv2.waitKey(wait_time_ms)

    @staticmethod
    def merge_imgs(imgs, row_col_num):
        """
        Merges all input images as an image with specified merge format.

        :param imgs : img list
        :param row_col_num : number of rows and columns displayed
        :return img : merges img
        """

        length = len(imgs)
        row, col = row_col_num

        assert row > 0 or col > 0, 'row and col cannot be negative at same time!'
        color = random_color(rgb=True).astype(np.float64)

        for img in imgs:
            cv2.rectangle(img, (0, 0), (img.shape[1], img.shape[0]), color)

        if row == 1 and col == -1:
            merge_imgs = np.hstack(imgs)
        elif row == -1 and col == 1:
            merge_imgs = np.vstack(imgs)
        else:
            if row == -1 and col != -1:
                row = math.ceil(len(imgs) / col)
            elif col == -1 and row != -1:
                col = math.ceil(len(imgs) / row)
            else:
                assert row * col >= length, 'Imgs overboundary, not enough windows to display all imgs!'

            fill_img_list = [np.zeros(imgs[0].shape, dtype=np.uint8)] * (row * col - length)
            imgs.extend(fill_img_list)
            merge_imgs_col = []
            for i in range(row):
                start = col * i
                end = col * (i + 1)
                merge_col = np.hstack(imgs[start: end])
                merge_imgs_col.append(merge_col)

            merge_imgs = np.vstack(merge_imgs_col)

        return merge_imgs

    @staticmethod
    # 可视化显示相关
    def show_bbox(image, bboxs_list, color=None,
                  thickness=1, font_scale=0.3, wait_time_ms=0, names=None,
                  is_show=True, is_without_mask=False):
        """
        Visualize bbox in object detection by drawing rectangle.

        :param image: numpy.ndarray.
        :param bboxs_list: list: [pts_xyxy, prob, id]: label or prediction.
        :param color: tuple.
        :param thickness: int.
        :param fontScale: float.
        :param wait_time_ms: int
        :param names: string: window name
        :param is_show: bool: whether to display during middle process
        :return: numpy.ndarray
        """
        assert image is not None
        font = cv2.FONT_HERSHEY_SIMPLEX
        image_copy = image.copy()
        for bbox in bboxs_list:
            if len(bbox) == 5:
                txt = '{:.3f}'.format(bbox[4])
            elif len(bbox) >= 6:
                txt = 'p={:.3f},id={:.3f}'.format(bbox[4], bbox[5])
            bbox_f = np.array(bbox[:4], np.int32)
            if color is None:
                colors = random_color(rgb=True).astype(np.float64)
            else:
                colors = color

            if not is_without_mask:
                image_copy = cv2.rectangle(image_copy, (bbox_f[0], bbox_f[1]), (bbox_f[2], bbox_f[3]), colors,
                                           thickness)
            else:
                mask = np.zeros_like(image_copy, np.uint8)
                mask1 = cv2.rectangle(mask, (bbox_f[0], bbox_f[1]), (bbox_f[2], bbox_f[3]), colors, -1)
                mask = np.zeros_like(image_copy, np.uint8)
                mask2 = cv2.rectangle(mask, (bbox_f[0], bbox_f[1]), (bbox_f[2], bbox_f[3]), colors, thickness)
                mask2 = cv2.addWeighted(mask1, 0.5, mask2, 8, 0.0)
                image_copy = cv2.addWeighted(image_copy, 1.0, mask2, 0.6, 0.0)
            if len(bbox) == 5 or len(bbox) == 6:
                cv2.putText(image_copy, txt, (bbox_f[0], bbox_f[1] - 2),
                            font, font_scale, (255, 255, 255), thickness=thickness, lineType=cv2.LINE_AA)
        if is_show:
            ImageHelper.show_img(image_copy, names, wait_time_ms)
        return image_copy
