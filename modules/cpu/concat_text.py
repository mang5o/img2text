import numpy as np


def concat_txt(txt_arr, cnt):
    tmp_txt = txt_arr.copy()
    for x in range(cnt - 1):
        txt_arr = np.concatenate((txt_arr, tmp_txt), axis=0)
    return txt_arr
