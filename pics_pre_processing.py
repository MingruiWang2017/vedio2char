"""
对图片进行处理：
为提高速度，可对图像进行下采样，但这里我们视频分辨率较低，不再调整；
"""
from PIL import Image
import os,sys

## 缩略图转化
def create_thumbnail(src_dir, dst_dir):
    pic_list = sorted(os.listdir(src_dir)) #获取文件加下的文件名列表

    for picture in pic_list:
        base_name = os.path.basename(picture) #获取当前图片名
        img = Image.open(os.path.join(src_dir, picture)) #读取图片
        size = (200, 200)
        img.thumbnail(size, Image.ANTIALIAS) #创建缩略图
        img.save(os.path.join(dst_dir, base_name)) #保存图片


if __name__ == "__main__":
    create_thumbnail("pics/", "thumb/")
    print("Down!")