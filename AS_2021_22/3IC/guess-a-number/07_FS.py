# Troppi import dal momento che te ne bastava uno!

from ast import Break
from doctest import OutputChecker
from importlib.resources import path
from random import seed
from random import randint
from unittest.mock import patch
from csv import reader
from itertools import count
from posixpath import split

# siccome in Python non c'e' il main, è sempre bene mettere dichiarato 
# varie funzioni (come si fa in C e C++ ad esempio). Questo permette
# di avere file più ordinati ed è anche più facile # trovare gli errori.
nomeGico = ("Guess a number")
print("+++++++++++++++++++++++++++")
print("| welcome to " + nomeGico + " |")
print("+++++++++++++++++++++++++++")
# If the number is positive, we print an appropriate message

out_path = "classifica.txt"
fo = open(out_path, "w")

count = 0
num_giocatori = input("Quanti giocatori? ")
num = input("Quale livello di difficolta: ")
while count != int(num_giocatori):
    count +=1
    conta_ten = 1
    if count >= 2:
        nickname = input("Next player, type your nickename: ")
    else:
        nickname = input("Please, type your nickename: ")
    print("Hi! " + nickname + ", Let's play together")
    # Sarebbe stato meglio pensare di usare un codice un pi' piu'
    # corto cercando di mettere dentro gli if e elif solo le cose
    # che cambiano veramente tra un livello di difficolta' ed un
    # altro.
    if int(num) == 1:
        print("Level " + num + " selected: Intermedio")
        list = 1
        listaVuota = []
        for i in range(list):
            value = randint(1, 9)
            listaVuota.append(value)
            print(value, end=' ') # !!!!!!! MOSTRA IL NUMERO DA INDOVINARE !!!!!
        tent = input("Inserisci un numero ")
        if int(tent) < listaVuota[0]:
            print("Inserisci un valore più alto")
        else:
            print("Inserisci un valore più basso")
        if int(tent) == listaVuota[0]:
            print("Complimenti hai indovinato al primo tentativo!!")
            print("Hai indovinato dopo", end=" "),print(conta_ten, end=" "),print(" tentativi.")
            conta_ten = 1
            fo.write(str(conta_ten) + "," + nickname + "\n")
            breakpoint
        else:
            while int(tent) != listaVuota[0]:
                conta_ten += 1
                tent = input("Tenta ancora: ")
                print("Numero di tentativi: ", end=" "),print(conta_ten)
                if int(tent) == listaVuota[0]:
                    print("Bravo!! Hai indovinato dopo", end=" "),print(conta_ten, end=" "),print(" tentativi.")
                    fo.write(str(conta_ten) + "," + nickname + "\n")
                    # la sintassi giusta è minuscolo! A te funziona perche' hai usato
                    # un import che ti e' stato suggerito da una IDE (es. Visual Studio Code),
                    # ma non e' corretto!
                    Break  
            
    if int(num) == 2:
        print("Level " + num + " selected: Avanzato")
        list = 1
        listaVuota = []
        for i in range(list):
            value = randint(10, 99)
            listaVuota.append(value)
            print(value, end=' ')
        tent = input("Inserisci un numero ")
        if int(tent) < listaVuota[0]:
            print("Inserisci un valore più alto")
        else:
            print("Inserisci un valore più basso")
        if int(tent) == listaVuota[0]:
            print("Complimenti hai indovinato al primo tentativo!!")
            print("Hai indovinato dopo", end=" "),print(conta_ten, end=" "),print(" tentativi.")
            conta_ten = 1
            fo.write(str(conta_ten) + "," + nickname + "\n")
            breakpoint
        else:
            while int(tent) != listaVuota[0]:
                conta_ten += 1
                tent = input("Tenta ancora: ")
                print("Numero di tentativi: ", end=" "),print(conta_ten)
                if int(tent) == listaVuota[0]:
                    print("Bravo!! Hai indovinato dopo", end=" "),print(conta_ten, end=" "),print(" tentativi.")
                    fo.write(str(conta_ten) + "," + nickname + "\n")
                    Break
        
    if int(num) == 3:
        print("Level " + num + " selected: Esperto")
        list = 1
        listaVuota = []
        for i in range(list):
            value = randint(100, 199)
            listaVuota.append(value)
            print(value, end=' ')
        tent = input("Inserisci un numero ")
        if int(tent) < listaVuota[0]:
            print("Inserisci un valore più alto")
        else:
            print("Inserisci un valore più basso")
        if int(tent) == listaVuota[0]:
            print("Complimenti hai indovinato al primo tentativo!!")
            print("Hai indovinato dopo", end=" "),print(conta_ten, end=" "),print(" tentativi.")
            conta_ten = 1
            fo.write(str(conta_ten) + "," + nickname + "\n")
            breakpoint
        else:
            while int(tent) != listaVuota[0]:
                conta_ten += 1
                tent = input("Tenta ancora: ")
                print("Numero di tentativi: ", end=" "),print(conta_ten)
                if int(tent) == listaVuota[0]:
                    print("Bravo!! Hai indovinato dopo", end=" "),print(conta_ten, end=" "),print(" tentativi.")
                    fo.write(str(conta_ten) + "," + nickname + "\n")
                    Break
        
    if int(num) == 4:
        print("Level " + num + " selected: Pro")
        list = 1
        listaVuota = []
        for i in range(list):
            value = randint(1000, 9999)
            listaVuota.append(value)
            print(value, end=' ')
        tent = input("Inserisci un numero ")
        if int(tent) < listaVuota[0]:
            print("Inserisci un valore più alto")
        else:
            print("Inserisci un valore più basso")
        if int(tent) == listaVuota[0]:
            print("Complimenti hai indovinato al primo tentativo!!")
            print("Hai indovinato dopo", end=" "),print(conta_ten, end=" "),print(" tentativi.")
            conta_ten = 1
            fo.write(str(conta_ten) + "," + nickname + "\n")
            breakpoint
        else:
            while int(tent) != listaVuota[0]:
                conta_ten += 1
                tent = input("Tenta ancora: ")
                print("Numero di tentativi: ", end=" "),print(conta_ten)
                if int(tent) == listaVuota[0]:
                    print("Bravo!! Hai indovinato dopo", end=" "),print(conta_ten, end=" "),print(" tentativi.")
                    fo.write(str(conta_ten) + "," + nickname + "\n")
                    Break
        
    if int(num) == 5:
        print("Level " + num + " selected: Legen..(don't move)..dario")
        list = 1
        listaVuota = []
        for i in range(list):
            value = randint(10000, 19999)
            listaVuota.append(value)
            print(value, end=' ')
        tent = input("Inserisci un numero ")
        if int(tent) < listaVuota[0]:
            print("Inserisci un valore più alto")
        else:
            print("Inserisci un valore più basso")
        if int(tent) == listaVuota[0]:
            print("Complimenti hai indovinato al primo tentativo!!")
            print("Hai indovinato dopo", end=" "),print(conta_ten, end=" "),print(" tentativi.")
            conta_ten = 1
            fo.write(str(conta_ten) + "," + nickname + "\n")
            breakpoint
        else:
            while int(tent) != listaVuota[0]:
                conta_ten += 1
                tent = input("Tenta ancora: ")
                print("Numero di tentativi: ", end=" "),print(conta_ten)
                if int(tent) == listaVuota[0]:
                    print("Bravo!! Hai indovinato dopo", end=" "),print(conta_ten, end=" "),print(" tentativi.")
                    fo.write(str(conta_ten) + "," + nickname + "\n")
                    Break

print("Classifica")
print("**********************************")
print("*\t  Scoreboard    \t*")
print("**********************************")

print("+--------------------------------+")
print("| Pos \t  Name  \t Attemps |")
print("+--------------------------------+")

out_path = "classifica.txt"
fo = open(out_path, "r")
riordinamento = []
for i in fo:
    spl = i.strip().split(",")
    riordinamento.append(spl)

riordinamento.sort()
conta = 0
pos = 1
for i in riordinamento:
    print("| " + str(pos), end="\t  ")
    print(riordinamento[conta][1], end="\t\t ")
    print(riordinamento[conta][0] + "   \t |")
    conta +=1
    pos +=1
fo.close

# Il tuo gioco mostra sempre il numero da indovinare!!
# Guardando il codice e facendo delle prove, mi sembra
# che il tuo sistema di salvare la classifica non
# funzioni perche' il file viene continuamente sovrascritto

# Ci sono altre cose da migliorare
# sopratutto l'uso dei commenti ed il nome delle variabili che non sono
# un grosso problema (ma piccolo) in un programma di 150 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti e nomi di
# variabili scelti bene.

