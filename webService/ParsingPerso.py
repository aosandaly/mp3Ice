import json, string
from demandeControle import demandeControle
from motAction import motAction
from http import HTTPStatus

COMMANDE_OK = HTTPStatus.OK
COMMANDE_INCORRECTE = HTTPStatus.BAD_REQUEST
COMMANDE_NON_RECONNUE = HTTPStatus.CONFLICT

class ParsingPerso:
    mots_similaire = {}
    i = 0
    def __init__(self):
        for commande, listeSimilaire in motAction.EQUIVALENT.items():
            for action in listeSimilaire:
                self.mots_similaire[action] = commande

    def parsingPhrase(self, phrase):

        phrase = self.phrase_elaguer(phrase)
        phraseParts = str.lower(phrase).split(" ")

        # phrase avec plus d'un mot sauf si le premier est une action
        if ((len(phraseParts) <= 1) & (self.findActionFirstWord(phraseParts) is None)):
            return demandeControle(code=COMMANDE_INCORRECTE)

        self.i = 0

        commande = self.findAction(phraseParts)

        if commande != None:
            NameMusique = self.findTitleMusic(phraseParts)

            dc = demandeControle()
            dc.commande = commande
            dc.code = COMMANDE_OK
            dc.NameMusique = NameMusique
            return dc
        else:
            return demandeControle(code=COMMANDE_NON_RECONNUE)

    def phrase_elaguer(self, phrase):
        phrase = str.lower(phrase)
        phrasePropre = str()
        # for c in phrase:
            # if c in string.ascii_lowercase or c in string.digits or c == ' ':
            #     phrasePropre += c;
        return phrase

    # si le premier mot est une action
    def findActionFirstWord(self, phraseParts):
        if phraseParts[0] in self.mots_similaire:
            return self.mots_similaire[phraseParts[0]]
        else:
            return None

    # premier mot reconnu comme une commande
    def findAction(self,phraseParts):
        for self.i in range(len(phraseParts)):
            mot = phraseParts[self.i]
            if mot in self.mots_similaire:
                commande = self.mots_similaire[mot]
                break
            else:
                commande = None
        return commande

    # Si la commande reconnue est le dernier mot --> le nom de la chanson est au debut
    def findTitleMusic(self, phraseParts):
        if self.i == (len(phraseParts) - 1):
            return " ".join(phraseParts[:self.i])
        else:
            return " ".join(phraseParts[self.i + 1:])