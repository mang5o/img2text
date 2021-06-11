import numpy as np


def concat_img(img_arr, cnt):
    img_arr = np.tile(img_arr, (1, cnt))
    return img_arr
