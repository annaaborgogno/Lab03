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
        for parola in paroleSbagliate:
            print(parola)

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