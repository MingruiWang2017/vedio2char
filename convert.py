import os,sys
from PIL import Image, ImageDraw, ImageFont

"""
将图片转换为字符图片：
1.将图片灰度化；
2.将灰度化后的图片的像素点用对应的字符替换；
3.将替换后的字符串转换为字符图片。
"""

# 1.读取图片，灰度化
def load_picture(filename):
    # Gray = R * 0.299 + G * 0.587 + B * 0.114
    img = Image.open(filename).convert("L") #灰度化
    (x,y) = img.size

    pixels = list(img.getdata()) #读取灰度值，转化为list(一维)
    img.close()
    return (pixels, x, y)


# 2.将灰度化图的每个像素点替换为对应字符
#symbols为字符列表，对应灰度的0-255（从黑到白）字符所占面积越来越小
symbols = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 为保证图片现实起来不太密集，我们每间隔一个像素来替换
def create_ascii_picture(pixels, dest_name, x_size, y_size):
    scale = 4 #长度扩大倍数
    border =1 #边框宽度

    interval_pixel = 2 #图片填充的间隔像素点数
    #创建新空白图像，指定为灰度图"L", 指定大小，和初始填充颜色255（白色）
    img = Image.new("L",
                    (x_size * scale + 2 * border,
                     y_size * scale + 2 * border),
                     255)
    
    fnt = ImageFont.truetype("ARIALUNI.ttf", int(scale * 3)) #其中ttf便是一种字体，通过指定来获取对应字体的字符
    t = ImageDraw.Draw(img)

    x = border
    y = border
    # 从pixels数组中获得当前未知的灰度值，按照字符的长度映射为对应字符
    for j in range(0, y_size, interval_pixel):
        for i in range(0, x_size, interval_pixel):
            t.text( (x,y),
                    symbols[ int(pixels[j * x_size + i] / 256 * len(symbols))], 
                    font=fnt,
                    fill = 0
                    )
            x += scale * interval_pixel
        x = border
        y += scale * interval_pixel

    # 3.将拼凑的字符图片保存
    img.save(dest_name,"JPEG")

if __name__ == "__main__":
    src_dir = "pics/"
    dst_dir = "char_pics/"
    pic_list = sorted(os.listdir(src_dir))#获取待处理图片列表
    print("图片转化中...")
    for picture in pic_list:
        #读取图片，灰度化，一维化
        filename = os.path.join(src_dir, picture)
        pixels, x_size, y_size = load_picture(filename)

        #转换为字符图片
        des_name = os.path.join(dst_dir, picture)
        create_ascii_picture(pixels, des_name, x_size, y_size)

    print("转换完成！")