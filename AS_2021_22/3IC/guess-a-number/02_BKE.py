import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

path = "classifica.txt"
num = 0
tentativo = 1
lev = ["Very Easy","Easy","Medium","Hard","Very Hard"]
print("Benvenuto su Indovina Numero!")


try:
    matrice = []
    f = open(path)
    # la classifica e' una unica per tutti i livelli di difficolta'
    for riga in f:
        lista = riga.strip().split(",")   
        matrice.append(lista)
    f.close()
    print("***************************")
    print("*       ScoreBoard(" + str(len(matrice)) + ")" + "     *")
    print("***************************")
    print("+-------------------------+")

    for lista in matrice:
        nome = lista[0]
        punteggio = lista[1]
        diff_num = lista[2]
        diff_str = lev[int(diff_num) - 1]
        print("| " + nome + " " + punteggio + " " + diff_str + " |")
   
   
except:
    print("Scoreboard: Errore nella lettura del file")
    

name = input("Inserisci il tuo nome! ")
print("Ciao " + name + " Giochiamo insieme!")
print("Scegliere il livello della difficoltà! " + "\n" + "1. Very Easy"+"\n"+ "2. Easy"+ "\n"+ "3. Medium" + "\n" + "4. Hard"+ "\n" + "5. Very Hard")
levs = int(input("Seleziona la difficoltà! "))
print("Difficoltà scelta: "+ lev[levs - 1])

# potevi usare la potenza 'math.pow' 10^1 - 1, 10^2 - 1, ...
# per esercizio ti suggerisco di provare a modificare il codice
if (levs == 1):
    num = random.randint(0,9)
    print("Indovina il numero tra 0 e 9 ")
elif (levs == 2):
    num = random.randint(10,99)
    print("Indovina il numero tra 10 e 99 ")
elif (levs == 3):
    num = random.randint(100,999)
    print("Indovina il numero tra 100 e 999 ")
elif (levs == 4):
    num = random.randint(1000,9999)
    print("Indovina il numero tra 1000 e 9999 ")
elif (levs == 5):
    num = random.randint(10000,99999)
    print("Indovina il numero tra 10000 e 99999 ")
    
    
indovino = int(input("Inserisci il numero da indovinare! "))
cercando = True
while(cercando):
    if (indovino == num):
        print("Numero trovato!")
        cercando = False
    if (indovino < num):
        print("Il numero che hai scelto è basso al numero da indovinare")
        indovino = int(input("Inserisci il numero da indovinare! "))
        tentativo += 1
    if (indovino > num):
        print("Il numero che hai scelto è alto al numero da indovinare")
        indovino = int(input("Inserisci il numero da indovinare! "))
        tentativo += 1
print("Numeri di tentativi fatti: " + str(tentativo))


f = open(path, "a")
f.write(name + "," + str(tentativo) + "," + str(levs) +"\n")
f.close()

# In generale il programma è fatto bene, ci sono alcune cose da migliorare
# sopratutto l'uso dei commenti ed il nome delle variabili che non sono
# un grosso problema (ma piccolo) in un programma di 150 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti e nomi di
# variabili scelti bene.

# Mancano la gestione degli errori (ad esempio
# quando non viene messo un intero per la difficolta') 

