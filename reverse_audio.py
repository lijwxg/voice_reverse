#! /usr/bin/env python
# __*__ coding:utf-8 __*__

# project:  media
# filename: reverse_audio.py
# date:     2020-04-05 12:58
from pydub import AudioSegment
from pydub.playback import play


def main(voice_file):
    try:
        # 读取后缀名
        ext = voice_file.split(".")[-1]
        voice = AudioSegment.from_file(voice_file, ext)

        backwards = voice.reverse()
        # 播放该文件, 根据pydub介绍, play方法优先使用simpleaudio库
        play(backwards)

        # 如果需要将音频输出, 则需要安装ffmpeg或者libav的依赖
        # 将倒放的音频存为 "倒放.mp3" 文件
        # backwards.export("倒放.mp3",format="mp3")
    except Exception as e:
        print("请确认文件后缀, 或者文件格式是否支持")
        print(e)


if __name__ == '__main__':
    file_name = r"./assert/demo.m4a"
    main(file_name)
