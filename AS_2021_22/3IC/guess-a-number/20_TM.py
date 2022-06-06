# generate random integer values
from random import seed
import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

print("+---------------------------+")
print("| Welcome to Guess a number |")
print("+---------------------------+")
print()
difficoltà=["Pivello","Principiante","Apprendista","Maestro","Gran Maestro"]
nome = input("Scrivi il tuo nickname: ")
print("Ciao",nome,"! Giochiamo!!")
livello = int(input("Seleziona il livello di difficoltà 1-5: "))
if(livello>5  or livello<1):
    while livello>5  or livello<1:
        print("Hai sbagliato ad inserire la difficoltà del livello, reinserisci ")
        livello = int(input("Seleziona il livello di difficoltà 1-5: "))
print("Livello: ",livello," -->",difficoltà[livello-1])
# potevi usare la potenza 'math.pow' 10^1 - 1, 10^2 - 1, ...
# per esercizio ti suggerisco di provare a modificare il codice
if (livello == 1):
    numero = random.randint(0,9)
    print("Indovina il numero tra 0 e 9 ")
elif (livello == 2):
    numero = random.randint(10,99)
    print("Indovina il numero tra 10 e 99 " )
elif (livello == 3):
    numero = random.randint(100,999)
    print("Indovina il numero tra 100 e 999 " )
elif (livello == 4):
    numero = random.randint(1000,9999)
    print("Indovina il numero tra 1000 e 9999 " )
elif (livello == 5):
    numero = random.randint(10000,99999)
    print("Indovina il numero tra 10000 e 99999 ")
condizione = True
cont=1
# Questa parte è identica a quella di un tuo compagno
# non serve nemmeno che ti dica chi!
while(condizione):
    print("Tentativo ",cont)
    tentativo = int(input( " guess my number: "))
    if(tentativo<numero):
        print("Sbagliato, prova un valore più alto ")
    elif(tentativo==numero):
        print("Bravo hai indovinato dopo ",cont," tentativi!")
        condizione=False
    elif(attempt>numero):
        print("Sbagliato, prova un valore più basso")
    contatore=contatore+1
    if(contatore>10):
        print("Vuoi arrenderti?")
        arrandersi = input("Scrivi Si o NO ")
        if(arrandersi=="Si"):
            print("Il valore corretto era ",numero)
            condizione=False

# Manca completamente la parte della classifica

# A me sembra che tu il programma non l'abbia neanch provato
# infatti ho giocato e subito mi è stato dato un errore

# Sbagliato, prova un valore più alto 
# Traceback (most recent call last):
#   File "20_TM.py", line 53, in <module>
#     contatore=contatore+1
# NameError: name 'contatore' is not defined