
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
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtInput = input().lower()
        sc.handleSentence(txtInput,"english")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtInput = input().lower()
        sc.handleSentence(txtInput,"spanish")
        continue

    if int(txtIn) == 4:
        print("Il traduttore è chiuso")
        break