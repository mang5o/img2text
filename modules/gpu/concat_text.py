import cupy as cp


def concat_txt_gpu(txt_arr, cnt):
    txt_arr = cp.tile(txt_arr, (cnt, 1))
    return txt_arr
