import os
import re
from tkinter import *
from tkinter import font
import ffmpeg
from pytube import YouTube
from pytube.contrib.playlist import Playlist

class app:
    def __init__(self,master=None):
        self.default_font = ('Calibri', '10')
        self.first_Container = Frame(master)
        self.first_Container['pady'] = 30
        self.first_Container['padx'] = 70
        self.first_Container.pack()

        self.second_Container = Frame(master)
        self.second_Container['pady'] = 20
        self.second_Container['padx'] = 70
        self.second_Container.pack()


        self.third_Container = Frame(master)
        self.third_Container['pady'] = 20
        self.third_Container.pack()

        self.fourth_Container = Frame(master)
        self.fourth_Container['pady'] = 20
        self.fourth_Container['padx'] = 70
        self.fourth_Container.pack()

        self.title = Label(self.first_Container, text = 'URL do video ou playlist para download')
        self.title['font'] = self.default_font
        self.title.pack()

        self.url_box = Entry(self.second_Container)
        self.url_box['font'] = self.default_font
        self.url_box.pack()

        self.download_button = Button(self.third_Container)
        self.download_button['font'] = self.default_font
        self.download_button['width'] = 12
        self.download_button['text'] = 'Download'
        self.download_button['command'] = self.find
        self.download_button.pack()       

        self.status = Label(self.fourth_Container, text='')
        self.status['font'] = self.default_font
        self.status.pack()


    def find(self):
        url = self.url_box.get()
        update = self.download_playlist(url)
        self.url_box['text'] = ''
        self.update_status(update)

    def update_status(self, text):
        self.status['text'] = text

    def download_unic(self, url):
        yt = YouTube(url)

        file = yt.streams.filter(only_audio=True).first()

        directory = '/home/felipe/PycharmProjects/Apps/BaixaYouTube/Downloads'

        out_file = file.download(output_path=directory)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        self.update_status(yt.title + '\n has been successfully downloaded.')


    def download_playlist(self, url):
        try:
            DOWNLOAD_DIR = '/home/felipe/PycharmProjects/Apps/BaixaYouTube/Downloads'

            playlist = Playlist(url)

            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

            if(len(playlist.video_urls) == 0):
                self.update_status('Video Unico')
                self.download_unic(url)
            else:
                self.update_status(f'Playlist com {len(playlist.video_urls)} videos')
                for url in playlist.video_urls:
                    self.download_unic(url)
        
        except:
            self.download_unic(url)

    def convert(file):
        print()
        

