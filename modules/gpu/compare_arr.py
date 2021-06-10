import cupy as cp
import numpy as np
import time

def text_compare_gpu(text_array, img_array, text_width, text_height, img_w, img_h):
    start_time = time.time()
    text_array = text_array.astype(float)
    img_array = img_array.astype(float)
    ov_array = cp.subtract(text_array, img_array)
    ov_array = (ov_array/255)**2
    tmp_cal = []
    ov_shape = ov_array.shape
    w_grid_cnt = int(ov_shape[1] / text_width)
    h_grid_cnt = int(ov_shape[0] / text_height)
    print("\t[preprocess compare]\t%fs" % (time.time() - start_time))
    start_time = time.time()
    for y_grid in range(h_grid_cnt):
        tmp_x_line = []
        for x_grid in range(w_grid_cnt):
            tmp_grid = ov_array[y_grid * text_height : (y_grid + 1) * text_height,x_grid*text_width: (x_grid+1)*text_width]
            tmp_x_line.append(tmp_grid.sum())
        tmp_cal.append(int(cp.array(tmp_x_line).argmin()))
    print("\t[after calc loss]\t\t%fs" % (time.time() - start_time))
    img_w_grid = int(img_w/text_width)
    img_h_grid = int(img_h/text_height)
    output_arr = np.reshape(tmp_cal, (img_w_grid, img_h_grid))
    output_arr = np.rot90(output_arr)
    output_arr = np.flipud(output_arr)

    return output_arr