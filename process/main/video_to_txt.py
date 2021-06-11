from modules.common.write_output_file import write_output_file
from modules.gpu.cupy_check import cupy_check
from modules.common.calc_good_txt import calc_good_txt
from modules.common.font_size_check import font_size_check
import cv2
import time


def vtt_cpu(font, font_size, video, txt_vertical_interval, debug, output_file):
    from modules.cpu.compare_arr import text_compare
    from modules.cpu.concat_img import concat_img
    from modules.cpu.concat_text import concat_txt
    from modules.cpu.frame_to_arr import frame_to_arr
    from modules.cpu.txt_to_arr import txt_to_arr
    txt_w, txt_h = font_size_check(font, font_size, txt_vertical_interval)
    txt_cnt, txt_arr = txt_to_arr(txt_w, txt_h, font, font_size, invert=False)
    cap = cv2.VideoCapture(video)
    orig_fps = cap.get(cv2.CAP_PROP_FPS)
    first_frame = True
    txt_conc_arr = []
    while cap.isOpened():
        first_time = time.time()
        ret, img = cap.read()
        if not ret:
            break
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_w, img_h, w_grid_cnt, h_grid_cnt, img_arr = frame_to_arr(gray_img, txt_w, txt_h)
        if first_frame:
            txt_conc_arr = concat_txt(txt_arr, w_grid_cnt * h_grid_cnt)
            first_frame = False
        img_conc_arr = concat_img(img_arr, txt_cnt)
        output_arr = text_compare(txt_conc_arr, img_conc_arr, txt_w, txt_h, img_w, img_h)
        txt_img = calc_good_txt(output_arr)
        now_screen = ""
        for i in txt_img:
            now_screen += i + "\n"

        if debug:
            time_float = time.time() - first_time
            now_screen += (
                "\n[DEVICE\t]\tCPU\t\t\t\t[TIME\t]\t%.3fs\t\t[OUTPUT\t]\t%d*%d\n"
                "[FPS\t]\t%.3f/sec\t\t[Src Fps]\t%d\t\t\t[FONT\t]\t%s (%dpx*%dpx)" % (
                    time_float, w_grid_cnt, h_grid_cnt,
                    1/time_float, orig_fps, font, txt_w, txt_h
                ))

        write_output_file(output_file,now_screen)


def vtt_gpu(font, font_size, video, txt_vertical_interval, debug, output_file):
    from modules.gpu.compare_arr import text_compare_gpu
    from modules.gpu.concat_img import concat_img_gpu
    from modules.gpu.concat_text import concat_txt_gpu
    from modules.gpu.frame_to_arr import frame_to_arr_gpu
    from modules.gpu.txt_to_arr import txt_to_arr_gpu
    txt_w, txt_h = font_size_check(font, font_size, txt_vertical_interval)
    txt_cnt, txt_arr = txt_to_arr_gpu(txt_w, txt_h, font, font_size, invert=False)
    cap = cv2.VideoCapture(video)
    orig_fps = cap.get(cv2.CAP_PROP_FPS)
    first_frame = True
    txt_conc_arr = []
    while cap.isOpened():
        first_time = time.time()
        ret, img = cap.read()
        if not ret:
            break
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_w, img_h, w_grid_cnt, h_grid_cnt, img_arr = frame_to_arr_gpu(gray_img, txt_w, txt_h)
        if first_frame:
            txt_conc_arr = concat_txt_gpu(txt_arr, w_grid_cnt * h_grid_cnt)
            first_frame = False
        img_conc_arr = concat_img_gpu(img_arr, txt_cnt)
        output_arr = text_compare_gpu(txt_conc_arr, img_conc_arr, txt_w, txt_h, img_w, img_h)
        txt_img = calc_good_txt(output_arr)
        now_screen = ""
        for i in txt_img:
            now_screen += i + "\n"

        if debug:
            time_float = time.time() - first_time
            now_screen += (
                    "\n[DEVICE\t]\tCPU\t\t\t\t[TIME\t]\t%.3fs\t\t[OUTPUT\t]\t%d*%d\n"
                    "[FPS\t]\t%.3f/sec\t\t[Src Fps]\t%d\t\t\t[FONT\t]\t%s (%dpx*%dpx)" % (
                        time_float, w_grid_cnt, h_grid_cnt,
                        1 / time_float, orig_fps, font, txt_w, txt_h
                    ))

        write_output_file(output_file, now_screen)


def vtt_process(font, font_size, img, txt_v_interval, gpu, debug, output_file):
    if gpu:
        cupy_available, cupy_code, cupy_msg = cupy_check()
        if debug:
            print(cupy_msg)
        if cupy_code != 1:
            gpu = False

    if gpu:
        vtt_gpu(font, font_size, img, txt_v_interval, debug, output_file)
    else:
        vtt_cpu(font, font_size, img, txt_v_interval, debug, output_file)

