import os,sys

#将转化后的图片拼接为视频
merge_ascii_vedio_cmd = "ffmpeg.exe -threads 2 -start_number 000001 -r 24 -i char_pics/%06d.jpeg -i audio.mp3 -vcodec mpeg4 char_vedio.mp4"
os.system(merge_ascii_vedio_cmd)