from modules.common.calc_good_txt import calc_good_txt
from modules.common.font_size_check import font_size_check
from modules.common.write_output_file import write_output_file
from modules.gpu.cupy_check import cupy_check
import time


def itt_cpu(font, font_size, img, txt_vertical_interval, debug, output_file):
    from modules.cpu.compare_arr import text_compare
    from modules.cpu.concat_img import concat_img
    from modules.cpu.concat_text import concat_txt
    from modules.cpu.img_to_arr import img_to_arr
    from modules.cpu.txt_to_arr import txt_to_arr
    first_time = time.time()
    txt_w, txt_h = font_size_check(font, font_size, txt_vertical_interval)
    txt_cnt, txt_arr = txt_to_arr(txt_w, txt_h, font, font_size, invert=False)
    img_w, img_h, w_grid_cnt, h_grid_cnt, img_arr = img_to_arr(img, txt_w, txt_h)
    txt_conc_arr = concat_txt(txt_arr, w_grid_cnt * h_grid_cnt)
    img_conc_arr = concat_img(img_arr, txt_cnt)
    output_arr = text_compare(txt_conc_arr, img_conc_arr, txt_w, txt_h, img_w, img_h)
    txt_img = calc_good_txt(output_arr)
    end_time = time.time()
    output_txt = ""
    if debug:
        output_txt += ("[DEVICE\t]\t\tCPU\n[TIME\t]\t\t%fs\n[FONT\t]\t\t%s (%dpx*%dpx)\n[OUTPUT\t]\t\t%d*%d\n" %
                       (end_time - first_time, font, txt_w, txt_h, w_grid_cnt, h_grid_cnt))
    for i in txt_img:
        output_txt += i + "\n"
    write_output_file(output_file, output_txt)


def itt_gpu(font, font_size, img, txt_vertical_interval, debug, output_file):
    from modules.gpu.compare_arr import text_compare_gpu
    from modules.gpu.concat_img import concat_img_gpu
    from modules.gpu.concat_text import concat_txt_gpu
    from modules.gpu.img_to_arr import img_to_arr_gpu
    from modules.gpu.txt_to_arr import txt_to_arr_gpu
    first_time = time.time()
    txt_w, txt_h = font_size_check(font, font_size, txt_vertical_interval)
    txt_cnt, txt_arr = txt_to_arr_gpu(txt_w, txt_h, font, font_size, invert=False)
    img_w, img_h, w_grid_cnt, h_grid_cnt, img_arr = img_to_arr_gpu(img, txt_w, txt_h)
    txt_conc_arr = concat_txt_gpu(txt_arr, w_grid_cnt * h_grid_cnt)
    img_conc_arr = concat_img_gpu(img_arr, txt_cnt)
    output_arr = text_compare_gpu(txt_conc_arr, img_conc_arr, txt_w, txt_h, img_w, img_h)
    txt_img = calc_good_txt(output_arr)
    end_time = time.time()
    output_txt = ""
    if debug:
        output_txt += ("[DEVICE\t]\t\tGPU\n[TIME\t]\t\t%fs\n[FONT\t]\t\t%s (%dpx*%dpx)\n[OUTPUT\t]\t\t%d*%d\n" %
                       (end_time - first_time, font, txt_w, txt_h, w_grid_cnt, h_grid_cnt))
    for i in txt_img:
        output_txt += i + "\n"
    write_output_file(output_file, output_txt)


def itt_process(font, font_size, img, txt_v_interval, gpu, debug, output_file):
    if gpu:
        cupy_available, cupy_code, cupy_msg = cupy_check()
        if debug:
            print(cupy_msg)
        if cupy_code != 1:
            gpu = False

    if gpu:
        itt_gpu(font, font_size, img, txt_v_interval, debug, output_file)
    else:
        itt_cpu(font, font_size, img, txt_v_interval, debug, output_file)
