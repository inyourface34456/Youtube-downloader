import youtube_dl
import time
import os 

vid_urls = []
av = str(input('Audio or video?'))

if (av != 'null'):
  ydl_opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
  }

while True:
  vid = str(input('What is the video url?\n>>> '))
  if (vid == 'stop'):
    break
  vid_urls.append(vid)


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(vid_urls)