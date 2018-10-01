import os,sys

#1.使用ffmpeg将音频从mp4文件中提取出来
slice_audio_cmd = "ffmpeg.exe -i vedio_.mp4 -vn audio.mp3"
os.system(slice_audio_cmd)
