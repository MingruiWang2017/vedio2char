import os,sys

# 2.将视频分割成若干图片
slice_pic_cmd = "ffmpeg.exe -i vedio_.mp4 -r 24 pics/%06d.jpeg" # pics是用来放图片的文件夹，需要提前建立
os.system(slice_pic_cmd)
