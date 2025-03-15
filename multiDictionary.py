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
        paroleSbagliate = []
        if (language == "italian"):
            parole = words.split(" ")
            for parola in parole:
                parolaR = rw.RichWord(parola)
                if self.diz_ita.__contains__(parola):
                    parolaR.corretta = True
                else:
                    paroleSbagliate.append(parola)
            return paroleSbagliate
        elif (language == "english"):
            parole = words.split(" ")
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
            for parola in parole:
                parolaR = rw.RichWord(parola)
                if self.diz_esp.__contains__(parola):
                    parolaR.corretta = True
                else:
                    paroleSbagliate.append(parola)
            print("Le parole sbagliate sono:")
            return paroleSbagliate

    def searchWordLinear(self, words, language):
        paroleTrovate = []
        if (language == "italian"):
            parole = words.split(" ")
            for parola in parole:
                if self.diz_ita.__contains__(parola):
                    paroleTrovate.append(parola)
        elif (language == "english"):
            parole = words.split(" ")
            for parola in parole:
                if self.diz_eng.__contains__(parola):
                    paroleTrovate.append(parola)
        elif (language == "spanish"):
            parole = words.split(" ")
            for parola in parole:
                if self.diz_esp.__contains__(parola):
                    paroleTrovate.append(parola)
        return paroleTrovate

    def searchWordDichotomic(self, words, language):
        dizionario = []
        paroleTrovate = []
        if language == "italian":
            dizionario = self.diz_ita
        elif language == "english":
            dizionario = self.diz_eng
        elif (language == "spanish"):
            dizionario = self.diz_esp

        parole = words.split(" ")
        for parola in parole:
            minimo = 0
            massimo = len(dizionario) - 1
            trovata = False

            while minimo <= massimo:
                indiceMedio = (massimo + minimo)//2 #in modo da ottenere un numero intero
                parolaMedia = dizionario[indiceMedio]

                if parola == parolaMedia:
                    trovata = True
                    paroleTrovate.append(parola)
                    break
                elif parola > parolaMedia:
                    minimo = indiceMedio + 1 #la ricerca si effettua sugli elementi precedenti
                else:
                    massimo = indiceMedio - 1 #la ricerca si effettua sugli elementi successivi

            if not trovata:
                print(f"La parola {parola} non è stata trovata nel dizionario")

        return paroleTrovate