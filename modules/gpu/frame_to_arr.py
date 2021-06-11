import cupy as cp
import numpy as np
from PIL import Image
from modules.cpu.img_preprocessing import img_preprocessing


def frame_to_arr_gpu(img_frame, t_width, t_height):
    img = Image.fromarray(img_frame)
    np_img = np.array(img)
    np_img = img_preprocessing(np_img)
    img = Image.fromarray(np_img)
    w = img.width
    h = img.height
    w_mod = w % t_width
    h_mod = h % t_height
    w = w - w_mod
    h = h - h_mod
    img = img.crop((0, 0, w, h))
    w_grid_cnt = int(w / t_width)
    h_grid_cnt = int(h / t_height)
    over_arr = []
    for x in range(w_grid_cnt):
        tmp_arr = []
        for y in range(h_grid_cnt):
            tmp_img = img.crop((x * t_width, y * t_height, (x + 1) * t_width, (y + 1) * t_height))
            if len(tmp_arr) == 0:
                tmp_arr = cp.asarray(tmp_img)
            else:
                tmp_arr = cp.concatenate((tmp_arr, cp.asarray(tmp_img)), axis=0)
        if len(over_arr) == 0:
            over_arr = cp.asarray(tmp_arr)
        else:
            over_arr = cp.concatenate((over_arr, cp.asarray(tmp_arr)), axis=0)
    return w, h, w_grid_cnt, h_grid_cnt, over_arr
