# pip install youtube_dl, the only dependency
# https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/YoutubeDL.py
# Documentation for the YoutubeDL class. Check 'Available options' to pass more options
# This script gets the url and extracts the mp3 format, removes the unique ID of Youtube.

import youtube_dl

class YT2MP3():

    def __init__(self):
        self.ydl = youtube_dl.YoutubeDL(self.getOptions())

    def hook(self,d):
        if d['status'] == 'finished':
            print("Done Downloading, Coverting Now...")

    def getOptions(self):
        return {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
        }],
        'progress_hooks' : [self.hook]
        }

    def startDownload(self,url):
        self.ydl.download([url])

downloader = YT2MP3()
url = input("Enter Youtube Url:")
downloader.startDownload(url)
