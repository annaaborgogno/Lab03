
import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input("Inserisci la lingua:")
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtInput = input().lower()
        print(sc.handleSentence(txtInput,"italian"))
        print("-------------------------------------------------")
        print(sc.handleSentenceLinear(txtInput,"italian"))
        print("-------------------------------------------------")
        print(sc.handleSentenceDichotomic(txtInput,"italian"))
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtInput = input().lower()
        print(sc.handleSentence(txtInput,"english"))
        print("-------------------------------------------------")
        print(sc.handleSentenceLinear(txtInput, "english"))
        print("-------------------------------------------------")
        print(sc.handleSentenceDichotomic(txtInput,"english"))
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtInput = input().lower()
        print(sc.handleSentence(txtInput,"spanish"))
        print("-------------------------------------------------")
        print(sc.handleSentenceLinear(txtInput, "spanish"))
        print("-------------------------------------------------")
        print(sc.handleSentenceDichotomic(txtInput,"spanish"))
        continue

    if int(txtIn) == 4:
        print("Il traduttore è chiuso")
        break