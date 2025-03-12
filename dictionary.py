class Dictionary:
    #classe che gestisce il dizionario di una singola lingua, legge il file e lo mette in una lista locale
    def __init__(self, dizionario=None):
        if dizionario is None:
            dizionario = {}
        self.dizionario = dizionario

    def loadDictionary(self,path):
        dizionarioLingua = []
        with open(path,'r', encoding="utf-8") as infile:
            for riga in infile:
                parola = ""
                for i in riga:
                    if i != "\n":
                        parola += i
                dizionarioLingua.append(parola)
            return dizionarioLingua

    def printAll(self):
        for riga in self.dizionario:
            print(riga)

    @property
    def dict(self):
        return self._dict
