import numpy as np

def calculate_rcc(img_array):
    red = img_array[:, :, 0].astype('float')
    green = img_array[:, :, 1].astype('float')
    blue = img_array[:, :, 2].astype('float')
    rcc = np.sum(red) / (np.sum(red) + np.sum(green) + np.sum(blue))
    return rcc