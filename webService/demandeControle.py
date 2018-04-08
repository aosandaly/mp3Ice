import json, string

class demandeControle:
    def __init__(self,commande='',NameMusique='',code=200):
        self.commande = commande
        self.NameMusique = NameMusique
        self.code = code

    def to_json(self):
        return self.__dict__