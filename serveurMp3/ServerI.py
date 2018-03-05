import app
from Music import Music
import vlc
import time
import glob
import ntpath
import os
from eyed3 import id3 #pip install eyeD3 eyeD3[display-plugin]


class ServerI(app.Server):

    def __init__(self):
        self.documents = []
        self.instance = ""
        self.addMusicAuto()
        # music = Music("MINIONS.mp3", "fref", "fre", "fre")
        #
        # self.addDocument(music)
        # self.addDocument(music)

    def addMusicAuto(self):
        # inputFilepath = 'path/to/file/foobar.txt'
        # filename_w_ext = os.path.basename(inputFilepath)
        # filename, file_extension = os.path.splitext(filename_w_ext)
        # # filename = foobar
        # # file_extension = .txt
        #
        # path, filename = os.path.split(path / to / file / foobar.txt)
        # # path = path/to/file
        # # filename = foobar.txt
        tag = id3.Tag()
        for path in glob.glob('musics\\*.mp3'):
            #print(os.path.splitext(ntpath.basename(path))[0])
            tag.parse(path)
            if tag.artist is not None:
                artist = tag.artist
            else:
                artist = ''

            if tag.genre is not None:
                genre = tag.genre.name
            else:
                genre = ''

            if tag.artist_url is not None:
                url = tag.artist_url.decode("utf-8")
                print(url)
            else:
                url = 'null'

            music = Music(os.path.splitext(ntpath.basename(path))[0],genre,artist,url)
            self.addDocument(music)


    def addDocument(self, music, current=None):
        self.documents.append(music)
        sLog = 'La musique à envoyé sur le serveur'
        return sLog

    def removeDocument(self, name, current=None):
        for document in self.documents:
            if document.name == name:
                self.documents.remove(document)
            sLog = 'La musique à été supprimée du serveur'
            return sLog

    def displayListMusic(self, current=None):
        return self.documents

    def searchDocument(self, attribute, name, current=None):
        result = []
        for document in self.documents:
            if getattr(document, attribute) == name:
                result.append(document)
        return result

    def downloadDocument(self, document, current=None):
        f = open("musics/MINIONS.mp3", "rb")
        data = f.read()
        return data

    def LibvlcPlayerPlay(self,current=None):
       print('test')
       chemin = "musics/"
       media_name = "MINIONS.mp3"
       sout = '#transcode{acodec=mp3,ab=128,channels=2,samplerate=44100}:http{dst=:8090/' + str(media_name)+'}'
       self.instance = vlc.Instance("--input-repeat=999999")
       # instance = vlc.Instance('--verbose 2'.split())
       # instance =vlc.Instance('--repeat')
       # instance = vlc.Instance('--input-repeat=-1', '--no-video-title-show', '--fullscreen', '--mouse-hide-timeout=0')
       # instance.vlc_inst.media_player_new()
       # instance.set_fullscreen(True)
       # instance.set(True)
       # todo: faire le broadcast uniquement sur le client qui le demande
       self.instance.vlm_add_broadcast("lecteur", chemin + media_name, sout, 0, [], True, False)
       self.instance.vlm_play_media("lecteur")

    def LibvlcPlayerStop(self,current=None):
        print("d")
        self.instance.vlm_stop_media("lecteur")