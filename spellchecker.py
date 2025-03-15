import datetime
import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi = md.MultiDictionary()

    def handleSentence(self, txtInput, language):
        tic = datetime.datetime.now()
        testo = replaceChars(txtInput)
        paroleSbagliate = md.MultiDictionary().searchWord(testo, language)
        toc = datetime.datetime.now()
        print(f"Le parole errate sono {len(paroleSbagliate)} in un tempo di {toc - tic} s")
        return paroleSbagliate


    def handleSentenceLinear(self, txtInput, language):
        tic = datetime.datetime.now()
        testo = replaceChars(txtInput)
        paroleTrovate = md.MultiDictionary().searchWordLinear(testo, language)
        toc = datetime.datetime.now()
        print(f"Le seguenti parole sono state trovate con la ricerca lineare in {toc - tic} s nel dizionario")
        return paroleTrovate

    def handleSentenceDichotomic(self, txtInput, language):
        tic = datetime.datetime.now()
        testo = replaceChars(txtInput)
        paroleTrovate = md.MultiDictionary().searchWordDichotomic(testo, language)
        toc = datetime.datetime.now()
        print(f"Le seguenti parole sono state trovate con la ricerca dicotomica in {toc - tic} s nel dizionario")
        return paroleTrovate

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_?{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text