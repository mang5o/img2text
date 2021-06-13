# img2text
### Rule-based image convertor

![LANG](https://img.shields.io/github/languages/top/mang5o/img2text?style=for-the-badge) ![SIZE](https://img.shields.io/github/languages/code-size/mang5o/img2text?style=for-the-badge)

![ISSUES](https://img.shields.io/github/issues/mang5o/img2text?style=for-the-badge) ![REQUESTS](https://img.shields.io/github/issues-pr/mang5o/img2text?style=for-the-badge)

![STARS](https://img.shields.io/github/stars/mang5o/img2text?style=for-the-badge) ![WATCH](https://img.shields.io/github/watchers/mang5o/img2text?style=for-the-badge)

## INSTALL
#### PYTHON REQUIREMENTS
requirements.txt

    numpy==1.20.3  
    opencv-python==4.5.2.54  
    Pillow==8.2.0



#### GPU (optional)
You should install CUPY with correct version.
https://docs.cupy.dev/en/stable/install.html


## DOCS
#### OPTION
|SHORT|LONG|DESCRIPTION|TYPE|REQUIRED|DEFAULT
|--|--|--|--|--|--|
|-g|--gpu|using GPUs|store_true|FALSE|FALSE|
|-v|--video|video input file|store_true|FALSE|FALSE|
|-d|--debug|print debug contents|store_true|FALSE|FALSE|
|-i|--file|input file path|store|TRUE||
|-f|--font|output font path|store|TRUE||
|-s|--fontsize|output font size|store|FALSE|12|
|-t|--txtInterval|output  text vertical interval|store|FALSE|4|

#### COMMAND
default (image)

    python i2t.py -i <input_file> -f <ttf_file>

example (video & debug mode)

    python i2t.py -vd -i <video_file> -f <ttf_file> -s 20

## PROCESS
#### PREPROCESS
There are no preprocessing in this code.
You can make own preprocess like historgram equalization at **modules/cpu(gpu)/img_preprocessing.py**

#### ARRAYLIZATION
Make image array
Make Text array
#### COMPARISON
After arraylization, code subtract image array from text array.
And power output for calculate pixel difference.
For all output array(after subtraction)'s grids, add values to derive the letter with the least pixel difference.
#### OUTPUT
example


## OUTPUT
#### HOW TO SEE
Output file will be placed in output/output
If you process a video file, It's updated every minute.
So, watch or tail this file is a one way to see output.

## TODO
#### OPTIMIZATION
The code does not seem to be using CUPY efficiently.


     # modules/gpu.compare_arr.py
    for y_grid in range(h_grid_cnt):  
    tmp_x_line = []  
    for x_grid in range(w_grid_cnt):  
        tmp_grid = ov_array[y_grid * text_height : (y_grid + 1) * text_height,x_grid*text_width: (x_grid+1)*text_width]  
        tmp_x_line.append(tmp_grid.sum())  
    tmp_cal.append(int(cp.array(tmp_x_line).argmin()))
Slicing array process like this is very slow, so I will change this comparison process to convolution.
Now GPU process is slower than CPU process.


#### PREPROCESS
Depending on the image, the preprocessing that produces good results varies.
I'm going to proceed with automating this.

## COMMENT
I didn't use Python as my main language, so I worked on this project just as a practice.  
I think it is essential for neural network, but I think it is better when rule-based model is available.  
ISSUES & PULL REQUESTS are always welcome. Thank you for your interest.
