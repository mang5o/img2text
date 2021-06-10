import numpy as np


def concat_txt(txt_arr, cnt):
    txt_arr = np.tile(txt_arr,(cnt,1))
    return txt_arr
