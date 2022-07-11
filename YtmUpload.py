import youtube_dl
from ytmusicapi import YTMusic
import os

def get_mp3(url_link):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = url_link, download = False
    )
    
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': f"{video_info['title']}.mp3",
    }
    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    
    res = f"{video_info['title']}.mp3"
    return res


def upload(src):
    ytmusic = YTMusic("headers_auth.json")
    YTMusic.upload_song(ytmusic, src)
    os.remove(src)
