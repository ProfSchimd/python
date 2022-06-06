## guesss a number
 
from importlib.resources import path
from operator import truediv
from random import randint
from tokenize import String

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene dichiarare varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.
 
print("inserire nome")
nome = input()
 
print(" BENVENUTO NEL GIOCO ")
print(nome)
# va bene, ma c'è anche modo di farlo con un solo file
path1 = "classifica1.txt"
path2 = "classifica2.txt"
path3 = "classifica3.txt"
path4 = "classifica4.txt"
path5 = "classifica5.txt"
print(" SELEZIONARE LA DIFFICOLTÀ DA 1 a 5")
lvl = int(input())
i = 0
n = 0
corretto = False
# Sarebbe stato meglio pensare di usare un codice un pi' piu'
# corto cercando di mettere dentro gli if e elif solo le cose
# che cambiano veramente tra un livello di difficolta' ed un
# altro.
if(lvl == 1):
    r = randint(1, 10)
    while(corretto == False):
        print("tentativo n°", String(i))
        n = input
        if(n == r):
            print("numero corretto")
            corretto = True
        elif(n < r):
            print("il numero da indovinare è più grande")
        elif(n > r):
            print("il numero da indovinare è più piccolo")
 
        i += 1
elif(lvl == 2):
    r = randint(1, 100)
    while(corretto == False):
        print("tentativo n°", String(i))
        n = input()
        if(n == r):
            print("numero corretto")
            corretto = True
        elif(n < r):
            print("il numero da indovinare è più grande")
        elif(n > r):
            print("il numero da indovinare è più piccolo")
 
        i += 1
elif(lvl == 3):
    r = randint(1, 1000)
    while(corretto == False):
        print("tentativo n°", String(i))
        n = input()
        if(n == r):
            print("numero corretto")
            corretto = True
        elif(n < r):
            print("il numero da indovinare è più grande")
        elif(n > r):
            print("il numero da indovinare è più piccolo")
 
        i += 1
elif(lvl == 4):
    r = randint(1, 10000)
    while(corretto == False):
        print("tentativo n°", String(i))
        n = input()
        if(n == r):
            print("numero corretto")
            corretto = True
        elif(n < r):
            print("il numero da indovinare è più grande")
        elif(n > r):
            print("il numero da indovinare è più piccolo")
 
        i += 1
elif(lvl == 5):
    r = randint(1, 100000)
    while(corretto == False):
        print("tentativo n°", String(i))
        n = input()
        if(n == r):
            print("numero corretto")
            corretto = True
        elif(n < r):
            print("il numero da indovinare è più grande")
        elif(n > r):
            print("il numero da indovinare è più piccolo")
 
        i += 1
       
if (int(lvl)) == 1:
    file_write = open(path1, "a")
    file_write.write(nome+ ", "+ (str(i))+ "\n")
    file_write.close()
    file_read = open(path1, "r")
    for scoreboard in file_read:
        print(scoreboard)
   
    file_read.close()
elif (int(lvl)) == 2:
    file_write = open(path2, "a")
    file_write.write(nome+ ", "+ (str(i))+ "\n")
    file_write.close()
    file_read = open(path2, "r")
    for scoreboard in file_read:
        print(scoreboard)
   
    file_read.close()
elif (int(lvl)) == 3:
    file_write = open(path3, "a")
    file_write.write(nome+ ", "+ (str(i))+ "\n")
    file_write.close()
    file_read = open(path3, "r")
    for scoreboard in file_read:
        print(scoreboard)
   
    file_read.close()
elif (int(lvl)) == 4:
    file_write = open(path4, "a")
    file_write.write(nome+ ", "+ (str(i))+ "\n")
    file_write.close()
    file_read = open(path4, "r")
    for scoreboard in file_read:
        print(scoreboard)
   
    file_read.close()
elif (int(lvl)) == 5:
    file_write = open(path5, "a")
    file_write.write(nome+ ", "+ (str(i))+ "\n")
    file_write.close()
    file_read = open(path5, "r")
    for scoreboard in file_read:
        print(scoreboard)
   
    file_read.close()
 
print("finito")

# Il programma non funziona, sono certo che non l'hai nemmeno
# provato perche' si vede subito che genera un errore come
# quello il seguente
# Traceback (most recent call last):
#   File "17_RL.py", line 26, in <module>
#     print("tentativo n°", String(i))
# TypeError: 'str' object is not callable

# Ci sono altre cose da migliorare
# sopratutto l'uso dei commenti ed il nome delle variabili che non sono
# un grosso problema (ma piccolo) in un programma di 150 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti e nomi di
# variabili scelti bene.
