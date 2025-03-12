import dictionary as di
import richWord as rw


class MultiDictionary:
    # gestisce l'accesso ai vari dizionari e implementa gli algoritmi di ricerca

    def __init__(self):
        self.diz_ita = di.Dictionary().loadDictionary("resources/Italian.txt")
        self.diz_eng = di.Dictionary().loadDictionary("resources/English.txt")
        self.diz_esp = di.Dictionary().loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        if (language == "italian"):
            self.diz_ita.printAll()
        elif (language == "english"):
            self.diz_eng.printAll()
        elif (language == "spanish"):
            self.diz_esp.printAll()

    def searchWord(self, words, language):
        if (language == "italian"):
            parole = words.split(" ")
            paroleSbagliate = []
            for parola in parole:
                parolaR = rw.RichWord(parola)
                if self.diz_ita.__contains__(parola):
                    parolaR.corretta = True
                else:
                    paroleSbagliate.append(parola)
            return paroleSbagliate
        elif (language == "english"):
            parole = words.split(" ")
            paroleSbagliate = []
            for parola in parole:
                parolaR = rw.RichWord(parola)
                if self.diz_eng.__contains__(parola):
                    parolaR.corretta = True
                else:
                    paroleSbagliate.append(parola)
            print("Le parole sbagliate sono:")
            return paroleSbagliate
        elif (language == "spanish"):
            parole = words.split(" ")
            paroleSbagliate = []
            for parola in parole:
                parolaR = rw.RichWord(parola)
                if self.diz_esp.__contains__(parola):
                    parolaR.corretta = True
                else:
                    paroleSbagliate.append(parola)
            print("Le parole sbagliate sono:")
            return paroleSbagliate