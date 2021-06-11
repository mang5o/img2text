import cupy as cp
from PIL import Image, ImageDraw, ImageFont
from config.config import get_available_letters


def txt_to_arr_gpu(width, height, font, font_size, invert=False):
    letters = get_available_letters()
    if invert:
        t_color = 0
        b_color = 255
    else:
        t_color = 255
        b_color = 0
    fnt = ImageFont.truetype(font, font_size, encoding="UTF-8")
    all_text = Image.new('L', (width * len(letters), height))
    for i in range(len(letters)):
        let_img = Image.new("L", (width, height), color=b_color)
        d = ImageDraw.Draw(let_img)
        w, h = fnt.getsize(letters[i])
        w_par = (width - w) / 2
        h_par = (height - h) / 2
        d.text((w_par, h_par), letters[i], font=fnt, fill=t_color)
        all_text.paste(let_img, (width*i, 0))
    txt_arr = cp.asarray(all_text)
    return len(letters), txt_arr
