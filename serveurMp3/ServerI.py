import app
from Music import Music
import vlc
import time

class ServerI(app.Server):

    def __init__(self):
        self.documents = []

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

    def testLibvlcPlayer(self,current=None):
       print('test')
       media_name = "MINIONS.mp3"
       sout = '#transcode{acodec=mp3,ab=128,channels=2,samplerate=44100}:http{dst=:8090/' + str(media_name)+'}'
       instance = vlc.Instance("")
       instance.vlm_add_broadcast("lecteur", media_name, sout, 0, [], True, False)
       instance.vlm_play_media("lecteur")
