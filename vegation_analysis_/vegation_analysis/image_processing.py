from PIL import Image
import numpy as np
import csv
from datetime import datetime
from .gcc_calculation import calculate_gcc
import glob
# 手动定义ROI坐标
roi_coords = (1516, 1164, 2453, 1632)  # 替换为实际的ROI坐标
def process_images(image_paths, roi_coords, output_csv_path):
    with open(output_csv_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # 添加BCC、RCC和BRI到CSV表头
        csvwriter.writerow(['Image', 'Date', 'Overall_GCC', 'ROI_GCC', 'Overall_BCC', 'ROI_BCC', 'Overall_RCC', 'ROI_RCC', 'Overall_BRI', 'ROI_BRI'])

        for image_path in image_paths:
            img = Image.open(image_path)
            img_array = np.array(img)

            # 计算整个图像和ROI的各项指数
            overall_gcc = calculate_gcc(img_array)
            roi_gcc = calculate_gcc(img_array[roi_coords[1]:roi_coords[3], roi_coords[0]:roi_coords[2], :])
            overall_bcc = calculate_bcc(img_array)
            roi_bcc = calculate_bcc(img_array[roi_coords[1]:roi_coords[3], roi_coords[0]:roi_coords[2], :])
            overall_rcc = calculate_rcc(img_array)
            roi_rcc = calculate_rcc(img_array[roi_coords[1]:roi_coords[3], roi_coords[0]:roi_coords[2], :])
            overall_bri = calculate_bri(img_array)
            roi_bri = calculate_bri(img_array[roi_coords[1]:roi_coords[3], roi_coords[0]:roi_coords[2], :])

            # 从文件名中提取年月日
            filename = image_path.split('/')[-1]
            date_str = '_'.join(filename.split('_')[2:5])
            date_obj = datetime.strptime(date_str, '%Y_%m_%d')
            date_formatted = date_obj.strftime('%Y-%m-%d')

            # 将结果写入CSV
            csvwriter.writerow([filename, date_formatted, overall_gcc, roi_gcc, overall_bcc, roi_bcc, overall_rcc, roi_rcc, overall_bri, roi_bri])


# 指定你的图像文件夹路径和输出CSV文件的路径
#image_folder = 'D:\\pycharm\\fenglinfigure1'  # 替换为你的图像文件夹路径
#output_csv_path = 'D:\\pycharm\\gcc_values.csv'  # 替换为输出CSV文件的路径
image_paths = glob.glob(f'{image_folder}/*.jpg')

# 处理图像并保存G值
process_images(image_paths, roi_coords, output_csv_path)

  # 请用之前讨论的process_images函数的实现来替换这个占位符
