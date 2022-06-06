import math
import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.
path = "classifica.txt"
f = open(path, "r")
difficulties = ["free", "ez", "ok", "wp", "notable"]
quotesbasso = ["Non l'hai azzeccato, prova con qualcosa di più alto",
               "Ahi! Non e' questo, riprova con un numero più alto", "Bruh- riprova con un numero più alto",
               "Hai sbagliato, ma puoi sempre riprovare con un numero più alto",
               "Wrong. Stai determinato, il numero è più alto", "E niente, sbagliato, il numero è più alto",
               "Nope. Più alto", "Se una cosa puo' andare male lo fara', riprova con un numero più alto",
               "Un vincitore e' un perdente che non si arrende, riprova con un numero più alto"]
quotesalto = ["Niente, prova ad abbassare", "Ahi! Non e' questo, riprova con un numero più basso",
              "Bruh- il numero è più basso", "Hai sbagliato, ma puoi sempre riprovare con un numero più basso",
              "Wrong. Stai determinato, il numero è più basso", "E niente, sbagliato, il numero è più basso",
              "Nope. Più basso", "Se una cosa puo' andare male lo fara', il numero è più basso btw",
              "Un vincitore e' un perdente che non si arrende, riprova con un numero più basso"]


def game(n, qa, qb):
    tries = 0
    # non era richiesto, ma manca la possibilita' di arrendersi...
    while (True):
        tries += 1
        tentativo = int(input("Tentativo numero " + str(int(tries)) + ": "))
        if tentativo == n:
            print("Esatto! Hai indovinato in " + str(int(tries)) + " tentativi")
            current = nick + ";" + str(tries)
            classifica(f, current, path, difficulty)
            break
        elif tentativo > n:
            print(qa[random.randint(0, len(qa) - 1)])
        elif tentativo < n:
            print(qb[random.randint(0, len(qb) - 1)])


def playerinfo():
    nickname = input("Inserici un nome per il giocatore: ")
    print("Fantastico " + nickname + "! Ci siamo quasi")
    print()
    return nickname


def diff():
    while (True):
        print(
            "Scegli un livello di difficolta'" + "\t\t" + "▓█████▄  ██▓  █████▒ █████▒██▓ ▄████▄   █    ██  ██▓  ▄▄▄█████▓▓██   ██▓")
        print(
            "1: free" + "\t\t\t\t\t\t\t\t\t" + "▒██▀ ██▌▓██▒▓██   ▒▓██   ▒▓██▒▒██▀ ▀█   ██  ▓██▒▓██▒  ▓  ██▒ ▓▒ ▒██  ██▒")
        print(
            "2: ez" + "\t\t\t\t\t\t\t\t\t" + "░██   █▌▒██▒▒████ ░▒████ ░▒██▒▒▓█    ▄ ▓██  ▒██░▒██░  ▒ ▓██░ ▒░  ▒██ ██░")
        print(
            "3: ok" + "\t\t\t\t\t\t\t\t\t" + "░▓█▄   ▌░██░░▓█▒  ░░▓█▒  ░░██░▒▓▓▄ ▄██▒▓▓█  ░██░▒██░  ░ ▓██▓ ░   ░ ▐██▓░")
        print(
            "4: wp" + "\t\t\t\t\t\t\t\t\t" + "░▒████▓ ░██░░▒█░   ░▒█░   ░██░▒ ▓███▀ ░▒▒█████▓ ░██████▒▒██▒ ░   ░ ██▒▓░")
        print(
            "5: notable" + "\t\t\t\t\t\t\t\t" + " ▒▒▓  ▒ ░▓   ▒ ░    ▒ ░   ░▓  ░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░      ██▒▒▒ ")
        print()
        # qui non c'è gestione dell'errore
        difficulty = int(input("Difficolta': "))
        if 0 < difficulty < 6:
            return difficulty
        else:
            print("Devi scegliere un numero compreso tra 1 e 5! Riprova")
            print()


def pensanumero(d, s):
    # molto bene!
    numero = random.randint((pow(10, d - 1)), pow(10, d) - 1)
    print("Ottimo! Hai scelto " + s[difficulty - 1])
    print()
    print("Ho pensato ad un numero fra " + str((pow(10, d - 1))) + " e " + str((pow(10, d)) - 1))
    print("Il tuo compito e' provare ad indovinarlo nel minor numero di tentativi")
    print()
    print("Pronto? Via!")
    print()
    return numero


# oltre a non usare i commenti, usi anche nomi delle
# variabili "anonime" che sono 'p' e 'd'. Tieni in conto
# che in Python non abbiamo neanche il tipo quindi p
# potrebbe tranquillamente significare Patate e d ...
def classifica(f, current, p, d):
    c = []
    dc = []
    d=d-1
    for r in f:
        # difficile capire cosa succede qui senza un minimo di commento
        # non mi riferisco solo a __contains__, ma a tutto quello che
        # fa il 'for'
        if r.__contains__(":"):
            c.append(dc)
            dc = []
        else:
            splitted = r.strip().split(";")
            dc.append(splitted)

    currents = current.strip().split(";")

    if int(c[d][len(c[d]) - 1][1]) < int(currents[1]):
        c[d].insert(len(c[d]), currents)

    for player in c[d]:
        if int(player[1]) > int(currents[1]):
            c[d].insert(c[d].index(player), currents)
            break

    print()
    print("++++++++++++++++++++++++")
    print("+    Classifica " + str(difficulty) + "     +")
    print("++++++++++++++++++++++++")
    print("Rank" + "\t" + "Name" + "\t" + "Tries")

    fo = open(p, "w")

    i = 0
    for dc in c:
        for player in c[i]:
            fo.write(str(player[0]) + ";" + str(player[1]) + "\n")
        i += 1
        fo.write(str(i) + ":" + "\n")

    f.close()
    fo.close()

    for player in c[d]:
        print(str(c[d].index(player) + 1) + "\t\t" + str(player[0]) + "\t" + str(player[1]))


def ascii():
    print(
        "  ▄████  █    ██ ▓█████   ██████   ██████     ▄▄▄          ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███")
    print(
        " ██▒ ▀█▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▒██    ▒    ▒████▄        ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒")
    print(
        "▒██░▄▄▄░▓██  ▒██░▒███   ░ ▓██▄   ░ ▓██▄      ▒██  ▀█▄     ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒")
    print(
        "░▓█  ██▓▓▓█  ░██░▒▓█  ▄   ▒   ██▒  ▒   ██▒   ░██▄▄▄▄██    ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ")
    print(
        "░▒▓███▀▒▒▒█████▓ ░▒████▒▒██████▒▒▒██████▒▒    ▓█   ▓██▒   ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒")
    print(
        " ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░    ▒▒   ▓▒█░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░")
    print(
        "  ░   ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░     ▒   ▒▒ ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░")
    print(
        "░ ░   ░  ░░░ ░ ░    ░   ░  ░  ░  ░  ░  ░       ░   ▒         ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░")
    print(
        "      ░    ░        ░  ░      ░        ░           ░  ░            ░    ░            ░    ░         ░  ░   ░     ")
    print("                                                                                        ░                 ")
    print()

# È sempre bene mettere un minimo di commenti alle varie parti a meno
# che queste non siano ovvie. Ad esempio: cosa fa la funzione ascii()?
# L'unica modo per rispodenre a questa domanda è guardare il codice
# perché non c'è né un breve commento alla chiamta, né un commento (breve
# o no) all'inizio della funzione. E se questa funzione fosse stata di 200
# righe anziché 20? Nel caso specifico di ascii() bastava usare un commento
# tipo 'stampa la ascii art guess a number'

ascii()
nick = playerinfo()
difficulty = diff()
numero = pensanumero(difficulty, difficulties)
game(numero, quotesalto, quotesbasso)

# In generale il programma è fatto bene, ci sono alcune cose da migliorare
# sopratutto l'uso dei commenti ed il nome delle variabili che non sono
# un grosso problema (ma piccolo) in un programma di 150 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti e nomi di
# variabili scelti bene.

# Il linguaggio è usato bene ed in alcuni punti hai anche usato alcune
# istruzioni/funzioni/metodi che non ho spiegato, quindi bene

# Ci sono delle cose che mancano come la gestione degli errori (ad esempio
# quando non viene messo un intero per la difficolta') ed anche un modo
# per arrendersi (non so se tu hai giocato al livello massimo e quanto
# sei dovuto andare avanti prima di terminare...)

