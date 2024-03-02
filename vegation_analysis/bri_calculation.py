import numpy as np

def calculate_bri(img_array):
    red = img_array[:, :, 0].astype('float')
    blue = img_array[:, :, 2].astype('float')
    bri = np.sum(blue) / np.sum(red)
    return bri