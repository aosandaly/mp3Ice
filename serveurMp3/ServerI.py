import app
from Music import Music

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