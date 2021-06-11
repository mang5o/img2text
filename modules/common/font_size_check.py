from PIL import ImageFont
from config.config import get_available_letters


def font_size_check(font, size, interval=0):
    font = ImageFont.truetype(font, size)
    w_max = 0
    h_max = 0
    for letter in get_available_letters():
        width = font.getsize(letter)[0]
        height = font.getsize(letter)[1]
        if w_max < width:
            w_max = width
        if h_max < height:
            h_max = height
    if w_max % 2 == 1:
        w_max += 1
    if h_max % 2 == 1:
        h_max += 1
    return w_max, h_max + interval
