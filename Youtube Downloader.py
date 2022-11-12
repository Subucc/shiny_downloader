from __future__ import unicode_literals
import tkinter as tk
from tkinter import filedialog
import youtube_dl
from colored import fg, attr

root = tk.Tk()
root.withdraw()

video_link = input('Type your video/playlist/channel link: ')
print('')

folder = filedialog.askdirectory()

ydl_opts = {'outtmpl': f'{folder}/%(title)s.%(ext)s', 'ignoreerrors': True, 'nooverwrites': True}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_link])

print('')
print ('%s -----------------  %s' % (fg(2), attr(0)))
print ('%s Download complete  %s' % (fg(2), attr(0)))
print ('%s -----------------   %s' % (fg(2), attr(0)))
print('')
input("Press enter to exit ;)")
