# mattexxino
import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

attempt = 1
Lista = []
cont = 0

# va bene, ma c'è anche modo di farlo con un solo file
path1 = "Leaderboard1.txt"
path2 = "Leaderboard2.txt"
path3 = "Leaderboard3.txt"
path4 = "Leaderboard4.txt"
path5 = "Leaderboard5.txt"

print("+---------------------------+")
print("| Welcome to Guess a Number |")
print("+---------------------------+")
print()

nickname = input("Please, type your nickname: ")
print()

print("Hi " + nickname + "! Let's play together")
print()

difficulty = input("Set difficulty level : ")
print()

print("Alright, you chose the " + difficulty + " difficulty!")
print()

# potevi usare la potenza 'math.pow' 10^1 - 1, 10^2 - 1, ...
# per esercizio ti suggerisco di provare a modificare il codice
if (int(difficulty)) == 1:
    num = random.randint(0, 10) # perche' da 0 a 10 e non da 0 a 9?
elif (int(difficulty)) == 2:
    num = random.randint(10, 99)
elif (int(difficulty)) == 3:
    num = random.randint(100, 999)
elif (int(difficulty)) == 4:
    num = random.randint(1000, 9999)
elif (int(difficulty)) == 5:
    num = random.randint(10000, 99999)

# print(num)

while True:
    print("Attempt " + (str(attempt)))
    user_input = input(nickname + " guess my number: ")
    print()

    if user_input == "q":
        print("You quit the game.")
        break
    if (int(user_input)) == num:
        print("Wow, you nailed it!")
        print()
        print(nickname + " won after " + (str(attempt)) + " attempts!")
        break
    # user_input è una stringa? allora str(user_input) non serve
    # user_input è un intero? allora int(user_input) non serve
    # in altre parole una delle due è inutile
    else:
        if (int(user_input)) < num:
            print("Sorry, my number is not " + (str(user_input)) + ", try a higher value!")
        else:
            print("Sorry, you have gone too high!")
        attempt += 1

print()

print("******************************")
print("*       Scoreboard(" + (str(difficulty)) + ")        *")
print("******************************")
print("+----------------------------+")
print("| Pos  Name         Attempts |")
print("+----------------------------+")

# Sarebbe stato meglio pensare di usare un codice un pi' piu'
# corto cercando di mettere dentro gli if e elif solo le cose
# che cambiano veramente tra un livello di difficolta' ed un
# altro.
if (int(difficulty)) == 1:
    fo = open(path1, "a")
    fo.write(nickname + ", " + (str(attempt)) + "\n")
    fo.close()
    fi = open(path1, "r")
    for leaderboard in fi:
        Lista.append(tuple(leaderboard.strip().split(", ")))
    Lista.sort(key=lambda x: x[1])
    for i in Lista:
        space = " "
        space2 = "    "
        cont += 1
        if cont <= 10:
            if len(i[0]) <= 7:
                tabs = "\t\t"
            else:
                tabs = "\t"
            if len(i[1]) > 1:
                space = ""
            if cont == 10:
                space2 = "   "
            print("| " + (str(cont)) + space2 + i[0] + tabs + i[1] + space + "       |")
        else:
            break
    print("+----------------------------+")
    fi.close()

elif (int(difficulty)) == 2:
    fo = open(path2, "a")
    fo.write(nickname + ", " + (str(attempt)) + "\n")
    fo.close()
    fi = open(path2, "r")
    for leaderboard in fi:
        Lista.append(tuple(leaderboard.strip().split(", ")))
    Lista.sort(key=lambda x: x[1])
    for i in Lista:
        space = " "
        space2 = "    "
        cont += 1
        if cont <= 10:
            if len(i[0]) <= 7:
                tabs = "\t\t"
            else:
                tabs = "\t"
            if len(i[1]) > 1:
                space = ""
            if cont == 10:
                space2 = "   "
            print("| " + (str(cont)) + space2 + i[0] + tabs + i[1] + space + "       |")
        else:
            break
    print("+----------------------------+")
    fi.close()

elif (int(difficulty)) == 3:
    fo = open(path3, "a")
    fo.write(nickname + ", " + (str(attempt)) + "\n")
    fo.close()
    fi = open(path3, "r")
    for leaderboard in fi:
        Lista.append(tuple(leaderboard.strip().split(", ")))
    Lista.sort(key=lambda x: x[1])
    for i in Lista:
        space = " "
        space2 = "    "
        cont += 1
        if cont <= 10:
            if len(i[0]) <= 7:
                tabs = "\t\t"
            else:
                tabs = "\t"
            if len(i[1]) > 1:
                space = ""
            if cont == 10:
                space2 = "   "
            print("| " + (str(cont)) + space2 + i[0] + tabs + i[1] + space + "       |")
        else:
            break
    print("+----------------------------+")
    fi.close()

elif (int(difficulty)) == 4:
    fo = open(path4, "a")
    fo.write(nickname + ", " + (str(attempt)) + "\n")
    fo.close()
    fi = open(path4, "r")
    for leaderboard in fi:
        Lista.append(tuple(leaderboard.strip().split(", ")))
    # immagino che tu non sappia cosa è una 'lambda expression'
    # quindi questo l'hai copiato da Internet...
    Lista.sort(key=lambda x: x[1]) 
    for i in Lista:
        space = " "
        space2 = "    "
        cont += 1
        if cont <= 10:
            if len(i[0]) <= 7:
                tabs = "\t\t"
            else:
                tabs = "\t"
            if len(i[1]) > 1:
                space = ""
            if cont == 10:
                space2 = "   "
            print("| " + (str(cont)) + space2 + i[0] + tabs + i[1] + space + "       |")
        else:
            break
    print("+----------------------------+")
    fi.close()

elif (int(difficulty)) == 5:
    fo = open(path5, "a")
    fo.write(nickname + ", " + (str(attempt)) + "\n")
    fo.close()
    fi = open(path5, "r")
    for leaderboard in fi:
        Lista.append(tuple(leaderboard.strip().split(", ")))
    Lista.sort(key=lambda x: x[1])
    for i in Lista:
        space = " "
        space2 = "    "
        cont += 1
        if cont <= 10:
            if len(i[0]) <= 7:
                tabs = "\t\t"
            else:
                tabs = "\t"
            if len(i[1]) > 1:
                space = ""
            if cont == 10:
                space2 = "   "
            print("| " + (str(cont)) + space2 + i[0] + tabs + i[1] + space + "       |")
        else:
            break
    print("+----------------------------+")
    fi.close()

# Il codice è scritto benino anche se non ha sfruttato al meglio
# gli if e gli elif. Ci sono alcune cose che sicuramente hai preso
# da Internet probabilmente senza veramente sapere cosa fanno e
# questo in generale non va bene perche' il mestiere del programmatore
# non e' quello che copiare di Internet, ma di risolvere i problemi
# con la propria capacita'. Ci sono alcune cose da migliorare
# sopratutto l'uso dei commenti ed il nome delle variabili che non sono
# un grosso problema (ma piccolo) in un programma di 150 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti e nomi di
# variabili scelti bene.

