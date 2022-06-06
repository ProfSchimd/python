import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene dichiarare varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

nomeGico = ("Indovina il Numero")
print("++++++++++++++++++++++++++++++++++")
print("| Benvenuto a " + nomeGico + " |")
print("++++++++++++++++++++++++++++++++++")
nome = input("Perfavore inserisci il tuo nickname: ")
print("Ciao, "+ nome+ ", cominciamo il gioco!")
difficolta = input("Per prima cosa scegli il livello di difficoltÃ  tra 1 a 5: ")
difficolta = int(difficolta)
# Sarebbe stato meglio pensare di usare un codice un pi' piu'
# corto cercando di mettere dentro gli if e elif solo le cose
# che cambiano veramente tra un livello di difficolta' ed un
# altro.
if difficolta == 1:
    print ("Difficolta Fallito")
    num = random.randint(1, 9)
    errore = 1
    indovina = None
    indovina = input("Cerca di indovinare il numero tra 1 e 9 ")
    indovina = int(indovina)
    while indovina != num:
        if indovina>num:
            errore = errore +1
            print("Il numero inserito è maggiore del numero da indovinare.")
        elif indovina<num:
            errore = errore +1
            print("Il numero inserito è minore del numero da indovinare.")
        indovina = input("Cerca di indovinare il numero tra 1 e 9 ")
        indovina = int(indovina)
    if indovina == num:
        print("Giusto!Il numero da indovinare era:", num)
        print("hai indovinato dopo" , errore , "tentativi")
if difficolta == 2:
    print ("Difficolta Fallito decente")
    num = random.randint(10, 99)
    indovina = None
    indovina = input("Cerca di indovinare il numero tra 10 e 99 ")
    indovina = int(indovina)
    while indovina != num:
        if indovina>num:
            errore = errore +1
            print("Il numero inserito è maggiore del numero da indovinare.")
        elif indovina<num:
            errore = errore +1
            print("Il numero inserito è minore del numero da indovinare.")
        indovina = input("Cerca di indovinare il numero tra 10 e 99 ")
        indovina = int(indovina)
    if indovina == num:
        print("Giusto!Il numero da indovinare era:", num)
        print("hai indovinato dopo" , errore , "tentativi")
if difficolta == 3:
    print ("Difficolta Quasi bravo")
    num = random.randint(100, 999)
    indovina = None
    indovina = input("Cerca di indovinare il numero tra 100 e 999 ")
    indovina = int(indovina)
    while indovina != num:
        if indovina>num:
            errore = errore +1
            print("Il numero inserito è maggiore del numero da indovinare.")
        elif indovina<num:
            errore = errore +1
            print("Il numero inserito è minore del numero da indovinare.")
        indovina = input("Cerca di indovinare il numero tra 100 e 999 ")
        indovina = int(indovina)
    if indovina == num:
        print("Giusto!Il numero da indovinare era:", num)
        print("hai indovinato dopo" , errore , "tentativi")
if difficolta == 4:
    print ("Difficolta Bravo")
    num = random.randint(1000, 9999)
    indovina = None
    indovina = input("Cerca di indovinare il numero tra 1000 e 9999 ")
    indovina = int(indovina)
    while indovina != num:
        if indovina>num:
            errore = errore +1
            print("Il numero inserito è maggiore del numero da indovinare.")
        elif indovina<num:
            errore = errore +1
            print("Il numero inserito è minore del numero da indovinare.")
        indovina = input("Cerca di indovinare il numero tra 1000 e 9999 ")
        indovina = int(indovina)
    if indovina == num:
        print("Giusto!Il numero da indovinare era:", num)
        print("hai indovinato dopo" , errore ,"tentativi")
if difficolta == 5:
    print ("Difficolta Bestia di satana")
    num = random.randint(10000, 99999)
    indovina = None
    indovina = input("Cerca di indovinare il numero tra 10000 e 99999 ")
    indovina = int(indovina)
    while indovina != num:
        if indovina>num:
            errore = errore +1
            print("Il numero inserito è maggiore del numero da indovinare.")
        elif indovina<num:
            errore = errore +1
            print("Il numero inserito è minore del numero da indovinare.")
        indovina = input("Cerca di indovinare il numero tra 10000 e 99999 ")
        indovina = int(indovina)
    if indovina == num:
        print("Giusto!Il numero da indovinare era:", num)
        print("hai indovinato dopo" , errore , "tentativi")

# Manca tutta la parte della classifica che non hai consegnato.

