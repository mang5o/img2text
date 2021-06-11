import argparse
import os

from process.main.img_to_txt import itt_process
from process.main.video_to_txt import vtt_process

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='image to text')

    parser.add_argument("-g", "--gpu",          dest="gpu",          action="store_true",   default=False)
    parser.add_argument("-v", "--video",        dest="video",        action="store_true",   default=False)
    parser.add_argument("-d", "--debug",        dest="debug",        action="store_true",   default=False)

    parser.add_argument("-i", "--file",         dest="file",         action="store",        default=   "")
    parser.add_argument("-f", "--font",         dest="font",         action="store",        default=   "")
    parser.add_argument("-s", "--fontsize",     dest="fontsize",     action="store",        default=   12)
    parser.add_argument("-t", "--txtInterval",  dest="txt_interval", action="store",        default=    4)

    args = parser.parse_args()

    if not os.path.exists("output"):
        os.mkdir("output")
    output_file = "output/output"

    now_error = False

    arg_gpu = args.gpu
    arg_video = args.video
    arg_debug = args.debug
    arg_file = args.file
    if not os.path.isfile(arg_file):
        print("[ERROR] input file is unavailable : " + arg_file)
        now_error = True
    arg_font = args.font
    if not os.path.isfile(arg_font):
        print("[ERROR] font file is unavailable : " + arg_font)
        now_error = True
    try:
        arg_fontsize = int(args.fontsize)
    except ValueError:
        print("[ERROR] fontsize option is invalid : " + args.fontsize)
        now_error = True
    try:
        arg_txt_interval = int(args.txt_interval)
    except ValueError:
        print("[ERROR] txt_interval option is invalid : " + args.txt_interval)
        now_error = True

    if not now_error:
        print(
            "┌─────────────┐\n" +
            "| img to text |\n" +
            "└─────────────┘\n" +
            "[DEVICE] " + ("CPU" if arg_gpu else "GPU") + "\n" +
            "[TYPE  ] " + ("VIDEO" if arg_video else "IMAGE") + "\n" +
            "[DEBUG ] " + str(arg_debug) + "\n" +
            "[INPUT ] " + arg_file + "\n" +
            "[FONT  ] " + arg_font + "\n" +
            "[F SIZE] " + str(arg_fontsize) + "\n" +
            "[T INTV] " + str(arg_txt_interval)
        )
        if arg_video:
            print("NOW PROCESSING")
            vtt_process(arg_font, arg_fontsize, arg_file, arg_txt_interval, arg_gpu, arg_debug, output_file)
        else:
            print("NOW PROCESSING")
            itt_process(arg_font, arg_fontsize, arg_file, arg_txt_interval, arg_gpu, arg_debug, output_file)

        print("ENDED")
