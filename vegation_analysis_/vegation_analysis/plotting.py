import matplotlib.pyplot as plt
import pandas as pd

def plot_vegation_scatter(csv_path):
    data = pd.read_csv(output_csv_path)

    # 绘制散点图
    plt.figure(figsize=(12, 6))

    # 整张图像的GCC散点图
    plt.subplot(1, 2, 1)
    plt.scatter(pd.to_datetime(data['Date']), data['Overall_GCC'], color='blue', label='Overall GCC')
    plt.gcf().autofmt_xdate()  # 自动格式化日期标签
    plt.title('Overall GCC Values')
    plt.xlabel('Date')
    plt.ylabel('GCC Value')
    plt.legend()

    # ROI的GCC散点图
    plt.subplot(1, 2, 2)
    plt.scatter(pd.to_datetime(data['Date']), data['ROI_GCC'], color='red', label='ROI GCC')
    plt.gcf().autofmt_xdate()
    plt.title('ROI GCC Values')
    plt.xlabel('Date')
    plt.ylabel('GCC Value')
    plt.legend()

    plt.tight_layout()
    plt.show()
    # 整张图像的BCC散点图
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(pd.to_datetime(data['Date']), data['Overall_BCC'], color='blue', label='Overall BCC')
    plt.gcf().autofmt_xdate()  # 自动格式化日期标签
    plt.title('Overall BCC Values')
    plt.xlabel('Date')
    plt.ylabel('BCC Value')
    plt.legend()

    # ROI的BCC散点图
    plt.subplot(1, 2, 2)
    plt.scatter(pd.to_datetime(data['Date']), data['ROI_BCC'], color='red', label='ROI BCC')
    plt.gcf().autofmt_xdate()
    plt.title('ROI BCC Values')
    plt.xlabel('Date')
    plt.ylabel('BCC Value')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # RCC
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(pd.to_datetime(data['Date']), data['Overall_RCC'], color='blue', label='Overall RCC')
    plt.gcf().autofmt_xdate()  # 自动格式化日期标签
    plt.title('Overall RCC Values')
    plt.xlabel('Date')
    plt.ylabel('RCC Value')
    plt.legend()

    # ROI的RCC散点图
    plt.subplot(1, 2, 2)
    plt.scatter(pd.to_datetime(data['Date']), data['ROI_RCC'], color='red', label='ROI RCC')
    plt.gcf().autofmt_xdate()
    plt.title('ROI RCC Values')
    plt.xlabel('Date')
    plt.ylabel('RCC Value')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # BRI图像
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(pd.to_datetime(data['Date']), data['Overall_BRI'], color='blue', label='Overall BRI')
    plt.gcf().autofmt_xdate()  # 自动格式化日期标签
    plt.title('Overall BRI Values')
    plt.xlabel('Date')
    plt.ylabel('BRI Value')
    plt.legend()

    # ROI的BRI散点图
    plt.subplot(1, 2, 2)
    plt.scatter(pd.to_datetime(data['Date']), data['ROI_BRI'], color='red', label='ROI BRI')
    plt.gcf().autofmt_xdate()
    plt.title('ROI BRI Values')
    plt.xlabel('Date')
    plt.ylabel('BRI Value')
    plt.legend()

    plt.tight_layout()
    plt.show()
