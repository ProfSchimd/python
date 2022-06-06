# Tutti questi import non servono a niente l'unico
# utile da usare era random!
from ast import Break
from doctest import OutputChecker
from importlib.resources import path
from random import seed
from random import randint
from unittest.mock import patch
from csv import reader
from itertools import count
from posixpath import split

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

gameName = ("Guess a number")
print("+++++++++++++++++++++++++++")
print("| welcome to " + gameName + " |")
print("+++++++++++++++++++++++++++")

out_path = "classifica.txt"
fileOutput = open(out_path, "w")

counter = 0
playerNumber = input("Quanti giocatori? ")
difficulty = input("Quale livello di difficolta: ")
while counter != int(playerNumber):
    counter +=1
    countToTen = 1
    if counter >= 2:
        playerName = input("Next player, type your nickename: ")
    else:
        playerName = input("Please, type your nickename: ")
    print("Hi! " + playerName + ", Let's play together")
    # Sarebbe stato meglio pensare di usare un codice un pi' piu'
    # corto cercando di mettere dentro gli if e elif solo le cose
    # che cambiano veramente tra un livello di difficolta' ed un
    # altro.
    if int(n) == 1: # 'n' -> ERRORE!!!!
        print("Level " + n + " selected: Intermedio")
        list = 1
        emptyList = []
        for i in range(list):
            value = randint(1, 9)
            emptyList.append(value)
            print(value, end=' ')
        inputTry = input("Inserisci un numero ")
        if int(inputTry) < emptyList [0]:
            print("Inserisci un valore più alto")
        else:
            print("Inserisci un valore più basso")
        if int(inputTry) == emptyList[0]:
            print("Complimenti hai indovinato al primo tentativo!!")
            print("Hai indovinato dopo", end=" "),print(countToTen, end=" "),print(" tentativi.")
            countToTen = 1
            fileOutput.write(str(countToTen) + "," + playerName + "\n")
            breakpoint
        else:
            while int(inputTry) != emptyList[0]:
                countToTen += 1
                inputTry = input("Tenta ancora: ")
                print("Numero di tentativi: ", end=" "),print(countToTen)
                if int(countToTen) == emptyList[0]:
                    print("Bravo!! Hai indovinato dopo", end=" "),print(countToTen, end=" "),print(" tentativi.")
                    fileOutput.write(str(countToTen) + "," + playerName + "\n")
                    Break
            
    if int(n) == 2:
        print("Level " + n + " selected: Avanzato")
        list = 1
        emptyList = []
        for i in range(list):
            value = randint(10, 99)
            emptyList.append(value)
            print(value, end=' ')
        inputTry = input("Inserisci un numero ")
        if int(inputTry) < emptyList[0]:
            print("Inserisci un valore più alto")
        else:
            print("Inserisci un valore più basso")
        if int(inputTry) == emptyList[0]:
            print("Complimenti hai indovinato al primo tentativo!!")
            print("Hai indovinato dopo", end=" "),print(countToTen, end=" "),print(" tentativi.")
            countToTen = 1
            fileOutput.write(str(countToTen) + "," + playerName + "\n")
            breakpoint
        else:
            while int(inputTry) != emptyList[0]:
                countToTen += 1
                inputTry = input("Tenta ancora: ")
                print("Numero di tentativi: ", end=" "),print(countToTen)
                if int(inputTry) == emptyList[0]:
                    print("Bravo!! Hai indovinato dopo", end=" "),print(countToTen, end=" "),print(" tentativi.")
                    fileOutput.write(str(countToTen) + "," + playerName + "\n")
                    Break
        
    if int(n) == 3:
        print("Level " + n + " selected: Esperto")
        list = 1
        emptyList = []
        for i in range(list):
            value = randint(100, 199)
            emptyList.append(value)
            print(value, end=' ')
        inputTry = input("Inserisci un numero ")
        if int(inputTry) < emptyList[0]:
            print("Inserisci un valore più alto")
        else:
            print("Inserisci un valore più basso")
        if int(inputTry) == emptyList[0]:
            print("Complimenti hai indovinato al primo tentativo!!")
            print("Hai indovinato dopo", end=" "),print(countToTen, end=" "),print(" tentativi.")
            countToTen = 1
            fo.write(str(CountToTen) + "," + playerName + "\n")
            breakpoint
        else:
            while int(inputTry) != emptyList[0]:
                countToTen += 1
                inputTry = input("Tenta ancora: ")
                print("Numero di tentativi: ", end=" "),print(countToTen)
                if int(inputTry) == emptyList[0]:
                    print("Bravo!! Hai indovinato dopo", end=" "),print(countToTen, end=" "),print(" tentativi.")
                    fo.write(str(countToTen) + "," + playerName + "\n")
                    Break
        
    if int(n) == 4:
        print("Level " + n + " selected: Pro")
        list = 1
        emptyList = []
        for i in range(list):
            value = randint(1000, 9999)
            emptyList.append(value)
            print(value, end=' ')
        inputTry = input("Inserisci un numero ")
        if int(inputTry) < emptyList[0]:
            print("Inserisci un valore più alto")
        else:
            print("Inserisci un valore più basso")
        if int(inputTry) == emptyList[0]:
            print("Complimenti hai indovinato al primo tentativo!!")
            print("Hai indovinato dopo", end=" "),print(countToTen, end=" "),print(" tentativi.")
            countToTen = 1
            fo.write(str(countToTen) + "," + playerName + "\n")
            breakpoint
        else:
            while int(inputTry) != emptyList[0]:
                countToTen += 1
                inputTry = input("Tenta ancora: ")
                print("Numero di tentativi: ", end=" "),print(countToTen)
                if int(inputTry) == emptyList[0]:
                    print("Bravo!! Hai indovinato dopo", end=" "),print(countToTen, end=" "),print(" tentativi.")
                    fileOutput.write(str(countToTen) + "," + playerName + "\n")
                    Break
        
    if int(n) == 5:
        print("Level " + n + " selected: Legendary")
        list = 1
        emptyList = []
        for i in range(list):
            value = randint(10000, 19999)
            emptyList.append(value)
            print(value, end=' ')
        inputTry = input("Inserisci un numero ")
        if int(inputTry) < emptyList[0]:
            print("Inserisci un valore più alto")
        else:
            print("Inserisci un valore più basso")
        if int(inputTry) == emptyList[0]:
            print("Complimenti hai indovinato al primo tentativo!!")
            print("Hai indovinato dopo", end=" "),print(countToTen, end=" "),print(" tentativi.")
            countToTen = 1
            fo.write(str(countToTen) + "," + playerName + "\n")
            breakpoint
        else:
            while int(countToTen) != emptyList[0]:
                countToTen += 1
                inputTry = input("Tenta ancora: ")
                print("Numero di tentativi: ", end=" "),print(countToTen)
                if int(inputTry) == emptyList[0]:
                    print("Bravo!! Hai indovinato dopo", end=" "),print(countToTen, end=" "),print(" tentativi.")
                    fileOutput.write(str(countToTen) + "," + playerName + "\n")
                    Break

print("**********************************")
print("*\t  Scoreboard    \t*")
print("**********************************")

print("+--------------------------------+")
print("| Pos \t  Name  \t Attemps |")
print("+--------------------------------+")

# mostru la classifica per tutti i livelli di difficolta'?
out_path = "classifica.txt"
fileOutput = open(out_path, "r")
rearrangement = []
for i in fo: # fo -> ERRORE!!!
    spl = i.strip().split(",")
    rearrangement.append(spl)

rearragement.sort()
counter = 0
position = 1
for i in rearragement:
    print("| " + str(position), end="\t  ")
    print(rearragement[counter][1], end="\t\t ")
    print(rearragement[counter][0] + "   \t |")
    counter +=1
    position +=1
fileOutput.close

# Il programma non funziona, probabilmente non l'hai nemmeno
# provato perche' altrimenti ti saresti accorto del problema
# Ho anche provato a correggere l'errore, ma ci sono stati
# altri problemi.
