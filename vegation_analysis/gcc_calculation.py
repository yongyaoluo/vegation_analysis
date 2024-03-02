import numpy as np

def calculate_gcc(img_array):
    red = img_array[:, :, 0].astype('float')
    green = img_array[:, :, 1].astype('float')
    blue = img_array[:, :, 2].astype('float')
    gcc = np.sum(green) / np.sum(red + green + blue)
    return gcc
    # 这里填入之前的calculate_gcc函数代码

