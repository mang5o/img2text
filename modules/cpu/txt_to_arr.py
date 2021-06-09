import numpy as np
from PIL import Image, ImageDraw, ImageFont
from config.config import get_available_letters


def txt_to_arr(width, height, font, font_size, invert=False):
    letters = get_available_letters()
    if invert:
        t_color = 0
        b_color = 255
    else:
        t_color = 255
        b_color = 0
    txt_arr = []
    fnt = ImageFont.truetype(font, font_size, encoding="UTF-8")
    for i in letters:
        let_img = Image.new("L", (width, height), color=b_color)
        d = ImageDraw.Draw(let_img)
        w, h = fnt.getsize(i)
        w_par = (width - w) / 2
        h_par = (height - h) / 2
        d.text((w_par, h_par), i, font=fnt, fill=t_color)
        let_txt_arr = np.asarray(let_img)
        if len(txt_arr) == 0:
            txt_arr = let_txt_arr
        else:
            txt_arr = np.concatenate((txt_arr, let_txt_arr), axis=1)
    return len(letters), txt_arr