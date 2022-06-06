import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

gioco = "Guess a number"
testoIniziale = "Benvenuto in " + gioco + "!"
print("+" + "-" * (len(testoIniziale) + 2) + "+")
print("| " + testoIniziale + " |")
print("+" + "-" * (len(testoIniziale) + 2) + "+" + "\n")

while True:
    name = input("Inserisci il tuo nickname: ")
    try:
        if(len(name)<=10):
            break
        else:
            print("Il nickname dev'essere di massimo 10 caratteri" + "\n")
    except:
        vuoto = 0

print("Ciao " + name + "! Cominciamo a giocare insieme!" + "\n")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -" + "\n")
print("Livello 1: Pivello - Numero generato dal numero 0 a 9")
print("Livello 2: Principiante - Numero generato dal numero 10 a 99")
print("Livello 3: Intermedio - Numero generato dal numero 100 a 999")
print("Livello 4: Maestro - Numero generato dal numero 1000 a 9999")
print("Livello 5: Gran Maestro - Numero generato dal numero 10000 a 99999" + "\n")

numeroInput = 0
difficoltà = ""
while True:
    numeroInput = input("Scegli un livello di difficoltà: ")
    try:
        # potevi usare la potenza 'math.pow' 10^1 - 1, 10^2 - 1, ...
        # per esercizio ti suggerisco di provare a modificare il codice
        if (int(numeroInput) == 1):
            print("Hai selezionato il livello 1. Pivello")
            nGenerato = random.randint(0, 9)
            difficoltà = "Pivello"
            break
            # print(nGenerato) Il numero generato non deve essere letto dall'utente ma è
            # utile in fase di debug per verificare che il numero generato sia
            # effettivamente del numero di cifre richiesto

        elif (int(numeroInput) == 2):
            print("Hai selezitononato il livello 2. Principiante")
            nGenerato = random.randint(10, 99)
            difficoltà = "Principiante"
            break
            # print(nGenerato)
        elif (int(numeroInput) == 3):
            print("Hai selezionato il livello 3. Intermedio")
            nGenerato = random.randint(100, 999)
            difficoltà = "Intermedio"
            break
            # print(nGenerato)
        elif (int(numeroInput) == 4):
            print("Hai selezionato il livello 4. Maestro")
            nGenerato = random.randint(1000, 9999)
            difficoltà = "Maestro"
            break
            # print(nGenerato)
        elif (int(numeroInput) == 5):
            print("Hai selezionato il livello 5. Gran Maestro")
            nGenerato = random.randint(10000, 99999)
            difficoltà = "Gran Maestro"
            break
            # print(nGenerato)
    except:
        print("\n" + "Attento! Non hai inserito un numero consentito. Riprova." + "\n")


tentativi = 0
numeroCasuale = 0
nIndovinato = False

maggiore = [", prova con un numero più piccolo!", ", vola più in basso!", ", scendi un po'!"]
minore = [", prova con un numero più grande!", ", vola più in alto!", ", sali un po'!"]
vittoria = [", complimenti!", ", sei un bomber!", ", sei troppo forte!", ", che fenomeno!"]
print("Se vuoi uscire dal gioco premi '#'")
while True:
    numeroCasuale = random.randint(0, 2)
    print("\n" + "Tentativi: " + (str(tentativi)) + "\n")
    input2 = input(name + " indovina il numero: ")
    try:
        if (input2 != '#'):
            input1 = int(input2)
        else:
            break
        if input1 == nGenerato:
            if tentativi == 0:
                tentativi += 1
                numeroCasuale = random.randint(0, 3)
                print(name + vittoria[numeroCasuale] + " Il numero era dunque " + (
                    str(nGenerato)) + " | Hai indovinato il numero dopo 1 tentativo!")
                nIndovinato = True
                break
            else:
                tentativi += 1
                numeroCasuale = random.randint(0, 3)
                print(name + vittoria[numeroCasuale] + " Il numero era dunque " + (
                    str(nGenerato)) + " | Hai indovinato il numero dopo " + (str(tentativi)) + " tentativi!" + "\n")
                nIndovinato = True
                break
        else:
            if (input1 < nGenerato):
                print("Il tuo numero non è " + (str(input1)) + minore[numeroCasuale])
            else:
                print("Il tuo numero non è " + (str(input1)) + maggiore[numeroCasuale])
            tentativi += 1
            continue
    except:
        print("\n" + "Attento! Non hai inserito un numero consentito. Riprova." + "\n")

if (nIndovinato):
    try:
        testo2 = "CLASSIFICA - DIFFICOLTÀ: "
        # *** MAI usare un path assoluto!!!!! ***
        path = r"C:\Users\Leonardo\Downloads\CLASSIFICA.txt"
        righe = 0
        f = open(path, "a")
        f.write(name + ", " + str(tentativi) + ", " + str(difficoltà)+ "\n")
        f.close()
        f = open(path, "r")
        for i in f:
            if (i.split(", ")[2] == str(difficoltà) + "\n"):
                    righe += 1
        f.close()

        lista1 = list(range(righe))
        k = 0
        f = open(path, "r")
        for i in f:
            if (i.split(", ")[2] == str(difficoltà) + "\n"):
                lista1[k] = tuple(i.split(", "))
                k += 1
        f.close()
        # come si chiama questo sotto? :P
        for i in range(len(lista1)):
            for j in range(i, len(lista1)):
                if (int(lista1[i][1]) > int(lista1[j][1])):
                    appoggio = lista1[i]
                    lista1[i] = lista1[j]
                    lista1[j] = appoggio

        print("*" + "*" * (len(testo2+difficoltà) + 2) + "*")
        print("* " + testo2 + difficoltà + " *")
        print("*" + "*" * (len(testo2+difficoltà) + 2) + "*")
        print("+" + ("-" * 23) + "+")
        print("| Pos Nome    Tentativi |")
        print("+" + ("-" * 23) + "+")
        for l in range(10):
            try:
                if l<9:
                    print("|", l + 1, " " + lista1[l][0] + (" ")*(18-len(lista1[l][0]+lista1[l][1])) + str(lista1[l][1] + " |"))
                else:
                    print("|", l + 1, lista1[l][0] + (" ")*(18-len(lista1[l][0]+lista1[l][1])) + str(lista1[l][1] + " |"))

            except:
                if l < 9:
                    print("|", l + 1, ("-")*20+"|")
                else:
                    print("|", l + 1, ("-")*19+"|")

        print("+" + ("-"*23) + "+")


    except:
        "Il file non è stato trovato"


else:
    print("Purtroppo non hai vinto... Andrà sicuramente meglio la prossima volta! Grazie per aver giocato!")

# In generale il programma è fatto bene, ci sono alcune cose da migliorare
# sopratutto l'uso dei commenti ed il nome delle variabili che non sono
# un grosso problema (ma piccolo) in un programma di 150 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti e nomi di
# variabili scelti bene.
