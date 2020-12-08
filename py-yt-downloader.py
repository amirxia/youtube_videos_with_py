import art
import colorama
import platform
import os
from pytube import YouTube

art.tprint("YouTube Video")
art.tprint("Py Downloader")

url = input(str(colorama.Fore.BLUE+"Put the URL of the video that you want to download: "))

try:
    youtube = YouTube(url)
    video = youtube.streams.first()
    opesys = platform.system()
    user = os.getlogin()
    print("Current OS: "+opesys)
    print("Current User: "+user)
    if(opesys == "Linux"):
        video.download('/home/'+user+'/Downloads')
        print(colorama.Fore.GREEN+"Video downloaded in /home/"+user+"/Downloads/")
        exit()
    elif(opesys == "Windows"):
        video.download('C:\\users\\'+user+'\\Downloads\\')
        print(colorama.Fore.GREEN+"Video downloaded in C:/users/"+user+"/Downloads/")
        exit()
except Exception as e:
    print(colorama.Fore.RED+"Error: put a valid URL!")
    print(e)
    exit()
