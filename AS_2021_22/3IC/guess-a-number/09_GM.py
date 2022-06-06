import pyfiglet

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

# Non era richiesto di usare librerie anche se non era esplicitamente
# vietato, l'idea era comunque quella di farvi far pratica con l'I/O
# facendo i vari compiti assegnati e ecostruendo il gioco poco per volta
# cosa che non mi sembra che tu abbia fatto
result = pyfiglet.figlet_format("Benvenuto in indovina il numero", font="speed")
print(result)
name = input(pyfiglet.figlet_format("scrivi il tuo nome", font="digital"))
print("Ciao " + name)
print(pyfiglet.figlet_format("il gioco prevede 5 livelli di difficoltà", font="digital"))
print("1 :Pricipiante")
print("2 :Professionista")
print("3 :maestro")
print("4 :Gran Maestro")
print("5 :Leggendario")
livello = input("Inserisci il livello di difficolta tra 1 e 5  " )
print (int(livello))
livello = (int(livello))
# a che serve la variabile 'livellostr' qui sotto?
livellostr = (int(livello)) 
if (livello > 5) or (livello == 0):
    print("Il levello non è valido")
    livello = input("Inserisci il livello di difficolta tra 1 e 5  " )
    print("Hai scelto il levello:")
    print (livello)
else:
    print("Hai scelto il levello: ")
    print (livello)
import random 
if (livello == 1):
    risultato = (random.randint(0,10))
    ciclo = 10
if (livello == 2):
    risultato = (random.randint(0,25))
    ciclo = 25
if (livello == 3):
    risultato = (random.randint(0,50))
    ciclo = 50
if (livello == 4):
    risultato = (random.randint(0,100))
    ciclo = 100
if (livello == 5):
    risultato = (random.randint(0,200))
    ciclo = 200
# print(risultato)
x=1
numero = input("Indovina il numero  ")
while (int(numero) != int(risultato)):
    xs=str(x)
    print("Tentavivo " + xs + "° non Hai vinto, riprova")
    if int(numero) > int(risultato):
        print("numero maggiore di quello da indovinare")
    else:
        print("numero minore di quello da indovinare")
    numero = input("Indovina il numero  ")
    x = x + 1
if (int(numero) == int(risultato)):
    print("Hai Vinto !!!! al " + str(x) + "° tentativo")
    riga = ""
    riga = str(livello) + "," +  str(x) + "," +  name  + " \n"
    print(riga)
    # La classifica è tutta mescolata (livello 1 e livello 5 insieme???)
    path = "classifica.txt"
    f = open(path,"a")
    f.write(riga)
    f.close()
    matrice = []
    f = open(path)
    for riga in f:
        lista = riga.strip().split(",")
        matrice.append(lista)
    f.close()
    print(matrice)
    