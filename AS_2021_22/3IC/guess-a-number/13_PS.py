import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

print()

diff=["Llv base","Lvl semibase","Lvl semisemibase","Lvl semisemisemibase","Lvl non base"]
nome = input("Come ti chiami: ")
print("WE",nome,"! vediamo se mi batterai...")
lvl = int(input("Scegli il livello di difficoltà (da 1 a 5): "))
if(lvl>5  or lvl<1):
    while lvl>5  or lvl<1:
        print("Inserisci un livello da 1 a 5: ")
        # manca la gestione degli errori, se l'utente non inserisce un intero il
        # programma termina con un errore
        lvl = int(input("Seleziona il livello di difficoltà (da 1 a 5): "))
dir = "classifica"+str(lvl)+".txt"
f = open(dir, "a")
print("livello: ",lvl," -->",diff[lvl-1])
# potevi usare la potenza 'math.pow' 10^1 - 1, 10^2 - 1, ...
# per esercizio ti suggerisco di provare a modificare il codice
if (lvl == 1):
    num = random.randint(0,9)
    print("Indovina il numero tra 0 e 9 ")
elif (lvl == 2):
    num = random.randint(10,99)
    print("Indovina il numero tra 10 e 99 " )
elif (lvl == 3):
    num = random.randint(100,999)
    print("Indovina il numero tra 100 e 999 " )
elif (lvl == 4):
    num = random.randint(1000,9999)
    print("Indovina il numero tra 1000 e 9999 " )
elif (lvl == 5):
    num = random.randint(10000,99999)
    print("Indovina il numero tra 10000 e 99999 ")
condizione = True
cont=1
while(condizione):
    print("Tentativo ",cont)
    tent = int(input( " guess my number: "))
    if(tent<num):
        print("Sbagliato, il numero è più alto ")
    elif(tent==num):
        print("Bravo! Hai indovinato in ",cont," tentativi")
        condizione=False
    elif(tent>num):
        print("Sbagliato, il numero più basso")
    cont=cont+1
    if(cont>10):
        print("Vuoi arrenderti?")
        resa = input("Scrivi Si o NO ")
        if(resa=="Si"):
            print("Il valore corretto era ",num)
            condizione=False
f.write(nome+":"+str(cont)+"\n")
f.close()

# Salvi la classifica, ma non la visualizza mai
