from config.config import get_available_letters


def calc_good_txt(output_arr):
    txt_img = []
    all_letters = get_available_letters()
    for i in range(len(output_arr)):
        new_tmp_img = ""
        for j in range(len(output_arr[i])):
            new_tmp_img += (all_letters[output_arr[i][j]])
        txt_img.append(new_tmp_img)

    return txt_img
