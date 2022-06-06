import random
# In generale è sempre buona norma dividere i file in
# funzioni anche se sono semplice. Questo permette poi
# di cambiare le cose in modo più semplice e veloce.
# Inoltre, quando il codice è diviso in pezzi più piccoli
# è più facile fare il 'debug' per trovare errori.
nomeGioco = "Guess a Number"
print("╔════════════════════════════╗")
print("║ Welcome to " + nomeGioco + "! ║")
print("╚════════════════════════════╝")
avanti = True
while(avanti):
    name = input("Please, insert your nickname: ")
    if(len(name) > 12):
        print("Il nome è troppo lungo (almeno 12 caratteri)")
    else:
        avanti = False
print("Howdy, " + name + "! It's time to play!")
print()
print("Difficulty(il numero corrisponde al numero di cifre da indovinare): 1 -> Pivello, 2 -> Principiante, 3 -> Normale, 4 -> Difficile, 5 -> Gran maestro.")
avanti = True
while (avanti):
    try:
        s = input("Select the difficulty for '" + name + "': ")
        difficulty = int(s)
        avanti = False
    except:
        print("Problem with converting " + s + " to a number")

difficulties = ["Pivello", "Principiante", "Normale", "Difficile", "Gran Maestro"]
print("You've selected the " + difficulties[difficulty - 1] + " difficulty")
nine = ""

# potevi usare la potenza 'math.pow' 10^1 - 1, 10^2 - 1, ...
# per esercizio ti suggerisco di provare a modificare il codice
for i in range(difficulty):
    nine += "9"
numero = random.randint(1*(10*(i)), int(nine))
#print(numero)

vittoria = False
attempt = 0
attempts = [5, 10, 15, 20, 25] # arresa automatica!!
while(not vittoria and attempt < attempts[difficulty - 1]):
    avanti = True
    attempt += 1
    print("Attempt " + str(attempt))
    while (avanti):
        try:
            risposta = input(name + " guess the number: ")
            rispostaInt = int(risposta)
            avanti = False
        except:
            print("Problem with converting " + risposta + " to a number")
    
    if(rispostaInt == numero):
        vittoria = True
    elif(rispostaInt < numero):
        print("Wrong number, try a higher number.")
    elif(rispostaInt > numero):
        print("Wrong number, try a lower number.")
    print()
        
if(vittoria):
    print()
    print("Victory!")
    print(name + " won in " + str(attempt) + " attempts.")
else:
    print("You've lost")
    
# va bene, ma c'è anche modo di farlo con un solo file
if(vittoria):    
    paths = ["classifica1.txt", "classifica2.txt", "classifica3.txt", "classifica4.txt", "classifica5.txt", ]
    
    
    fw = open(paths[difficulty - 1], "a")
    fw.write(name + "," + str(attempt) + "\n")
    fw.close()
    
    fr = open(paths[difficulty - 1], "r")
    lista_tuple = []
    for riga in fr:
        lista_tuple.append(tuple(riga.strip().split(",")))
    fr.close()
    lista_tuple.sort(key = lambda x: x[1])
       
    print()
    print("***************************")
    print("*      Scoreboard (" + str(difficulty) + ")     *")
    print("***************************")
    print("+-------------------------+")
    print("| Pos  Name       Attemps |")
    print("+-------------------------+")
    cont = 0
    for i in lista_tuple:
        spazio = " "
        if(cont < 10):
            if(len(i[0]) <= 7):
                tabulazioni = "\t\t"
            else:
                tabulazioni = "\t"
            if(len(i[1]) > 1):
                spazio = ""
            if(i[0] == name and i[1] == str(attempt)):
                print("| " + str(cont + 1) + "    " + i[0] + tabulazioni + i[1] + spazio + "|  <--- You!")
            else:
                print("| " + str(cont + 1) + "    " + i[0] + tabulazioni + i[1] + " |")
            cont += 1
    print("+-------------------------+")

# In generale il programma è fatto bene, ci sono alcune cose da migliorare
# sopratutto l'uso dei commenti ed il nome delle variabili che non sono
# un grosso problema (ma piccolo) in un programma di 150 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti e nomi di
# variabili scelti bene.
    