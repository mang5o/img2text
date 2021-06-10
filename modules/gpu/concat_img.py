import cupy as cp


def concat_img_gpu(img_arr, cnt):
    img_arr = cp.tile(img_arr,(1,cnt))
    return img_arr
