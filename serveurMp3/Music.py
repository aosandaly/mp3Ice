import app

# file musique (metaDataMusic)
class Music(app.music):
    def __init__(self, name, genre, author, url):
        self.name = name
        self.genre = genre
        self.author = author
        self.url = url