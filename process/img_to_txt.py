from modules.calc_good_txt import calc_good_txt
from modules.compare_arr import text_compare
from modules.concat_img import concat_img
from modules.concat_text import concat_txt
from modules.font_size_check import font_size_check
from modules.img_to_arr import img_to_arr
from modules.txt_to_arr import txt_to_arr
import time


def img_to_txt(font, font_size, img, txt_vertical_interval=0):
    start_time = time.time()
    txt_w, txt_h = font_size_check(font, font_size, txt_vertical_interval)
    print("[font_size_check]\t%fs"%(time.time()-start_time))
    start_time = time.time()
    txt_cnt, txt_arr = txt_to_arr(txt_w, txt_h, font, font_size, invert=False)
    print("[txt_to_arr]\t\t%fs"%(time.time()-start_time))
    start_time = time.time()
    img_w, img_h, w_grid_cnt, h_grid_cnt, img_arr = img_to_arr(img, txt_w, txt_h)
    print("[img_to_arr]\t\t%fs"%(time.time()-start_time))
    start_time = time.time()
    txt_conc_arr = concat_txt(txt_arr, w_grid_cnt*h_grid_cnt)
    print("[concat_txt]\t\t%fs"%(time.time()-start_time))
    start_time = time.time()
    img_conc_arr = concat_img(img_arr, txt_cnt)
    print("[concat_img]\t\t%fs"%(time.time()-start_time))
    start_time = time.time()
    output_arr = text_compare(txt_conc_arr, img_conc_arr, txt_w, txt_h, img_w, img_h)
    print("[text_compare]\t\t%fs"%(time.time()-start_time))
    start_time = time.time()
    txt_img = calc_good_txt(output_arr)
    print("[calc_good_txt]\t\t%fs"%(time.time()-start_time))
    for i in txt_img:
        print(i)


img_to_txt("../ttf_font/Ubuntu-Regular.ttf", 6, "../input/tb.jpeg", 4)
