import numpy as np


def text_compare(text_array, img_array, text_width, text_height, img_w, img_h):
    text_array = text_array.astype(float)
    img_array = img_array.astype(float)
    ov_array = np.subtract(text_array, img_array)
    ov_array = (ov_array/255)**2
    tmp_cal = []
    ov_shape = ov_array.shape
    w_grid_cnt = int(ov_shape[1] / text_width)
    h_grid_cnt = int(ov_shape[0] / text_height)
    for y_grid in range(h_grid_cnt):
        tmp_x_line = []
        for x_grid in range(w_grid_cnt):
            tmp_grid = ov_array[y_grid * text_height: (y_grid + 1) * text_height,
                       x_grid * text_width: (x_grid + 1) * text_width]
            tmp_x_line.append(tmp_grid.sum())
        tmp_cal.append(np.array(tmp_x_line).argmin())
    img_w_grid = int(img_w/text_width)
    img_h_grid = int(img_h/text_height)
    output_arr = np.reshape(tmp_cal, (img_w_grid, img_h_grid))
    output_arr = np.rot90(output_arr)
    output_arr = np.flipud(output_arr)

    return output_arr
