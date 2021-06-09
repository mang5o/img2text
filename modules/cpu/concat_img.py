import numpy as np


def concat_img(img_arr, cnt):
    tmp_img = img_arr.copy()
    for x in range(cnt - 1):
        img_arr = np.concatenate((img_arr, tmp_img), axis=1)
    return img_arr
