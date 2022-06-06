import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

game = "Guess a Number"
print("+-----------------------------+")
print("| Benvenuto in " + game + " |")
print("+-----------------------------+" + "\n")
name = input("Inserisci il tuo nickname: ")
print("Ciao " + name + "! Comiciamo il gioco!")
print("Seleziona il livello di difficolta del gioco selezionando un numero da 1 a 5" + "\n")
try:
    # potevi usare la potenza 'math.pow' 10^1 - 1, 10^2 - 1, ...
    # per esercizio ti suggerisco di provare a modificare il codice
    s = input("Inserisci il livello di difficoltà: ")
    if(int(s) == 1):
        print("Livello principiante" + "\n")
        a = random.randint(0,5)
    elif(int(s) == 2):
        print("Livello intermedio" + "\n")
        a = random.randint(0, 10)
    elif(int(s) == 3):
        print("Livello avanzato" + "\n")
        a = random.randint(0, 25)
    elif(int(s) == 4):
        print("Livello maestro" + "\n")
        a = random.randint(0, 50)
    elif(int(s) == 5):
        print("Livello gran maestro" + "\n")
        a = random.randint(0, 100)  
except:
    print("erroe riprova")
   
i = 0
while True:
    i+=1
    print ("Tentativo " + str(i))
    numero = input("inserisci un numero: ")
    if (str(numero) == "q"):
        break
    elif(int(numero) > a):
        print("Il numero è più piccolo" + "\n")
    elif(int(numero) < a):
        print("Il numero è più grande" + "\n")
    elif(int (numero) == a):
        print("Hai vinto al " + str(i) + " tentativo!!!!")
        break
   
path = "Classifica.txt"
f = open(path,"a")
f.write(str(name) + ";" + str(i) + ";" + "\n")
f.close()
f = open(path,"r")
righe = 0
for riga in f:
    if(riga.split(";")[2] == str(i)+ "\n"):
        righe+=1        
f.close
tupleList = list(range(righe))
y = 0
f = open(path)
for riga in f:
    if(riga.split(";")[2] == str(i)+ "\n"):
        tupleList[y] = tuple(riga.split(";"))
        y+=1
f.close # ERRORE! close()

# La classifica mostrata è un po' strana perche' mi mostra
# sempre gli stessi 10 punteggi anche se ce ne sono meno
print("********************************************")
print("*                Classifica                *")
print("********************************************")
print("+------------------------------------------+")
print("|Posizione   Nome                Tentativi |")
print("+------------------------------------------+")
for p in range(10): 
    print("|" + str(p+1) +  "\t     " + str(name) + "\t         " + str(i) + "         |")
print("+------------------------------------------+")

# Programma scritto benino anche se contiene qualche errore
# sia di sintassi sia di logica (vedi problema con
# classifica).

# Manca la gestione degli errori (esempio non inseirsco un
# intero come livello).




