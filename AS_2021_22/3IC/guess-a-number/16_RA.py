import random
# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

classifica = []
while(True):
    nome = "Guess a number"
    print ("Hi new player, Welcome to " + nome)
    nickname = input("What's your nickname? ")
    print ("\n" + "(っ◔◡◔)っ hi " + nickname + ", now try guessing a number, but first,")
    tentativi = 1
    s =  int(input("What would you like the difficulty to be: " + "\n" + "\n" + "1. ⓔⓐⓢⓨ"+"\n"+ "2. ⓝⓞⓣ ⓢⓞ ⓗⓐⓡⓓ"+ "\n"+ "3. ⓗⓐⓡⓓ" + "\n" + "4. ⓚⓘⓝⓓⓐ ⓗⓐⓡⓓ"+ "\n" + "5. ⓜⓐⓓⓝⓔⓢⓢ" + "\n"))
    # Sarebbe stato meglio pensare di usare un codice un pi' piu'
    # corto cercando di mettere dentro gli if e elif solo le cose
    # che cambiano veramente tra un livello di difficolta' ed un
    # altro.
    if(s == 1):
        print("You have choosen level: ⓔⓐⓢⓨ")
        numbero = random.randint(0,9)
        print (numbero)
        num = int(input("Try guessing the number now "))
        while(int(num) != numbero):
            if(int(num) < int(numbero)):
                print("Little hint, the number is higher than your previews attempt")
            else:
                print("Little hint, the number is lower than your previews attempt")
            num = input("Try again!")
            tentativi += 1
        print("You did it!!!" + "\n" + "Number of attempts: " + str(tentativi) + "\n")
    elif(s == 2):
        print("You have choosen level: ⓝⓞⓣ ⓢⓞ ⓗⓐⓡⓓ")
        numbero = random.randint(10,99)
        num = int(input("Try guessing the number now "))
        while(int(num) != numbero):
            if(int(num) < int(numbero)):
                print("Little hint, the number is higher than your previews attempt")
            else:
                print("Little hint, the number is lower than your previews attempt")
            num = input("Try again!")
            tentativi += 1
        print("You did it!!!" + "\n" + "Number of attempts: " + str(tentativi) + "\n")
    elif(s == 3):
        print("You have choosen level: ⓗⓐⓡⓓ")
        numbero = random.randint(100,999)
        num = int(input("Try guessing the number now "))
        while(int(num) != numbero):
            if(int(num) < int(numbero)):
                print("Little hint, the number is higher than your previews attempt")
            else:
                print("Little hint, the number is lower than your previews attempt")
            num = input("Try again!")
            tentativi += 1
        print("You did it!!!" + "\n" + "Number of attempts: " + str(tentativi) + "\n")
    elif(s == 4):
        print("You have choosen level: ⓚⓘⓝⓓⓐ ⓗⓐⓡⓓ")
        nubero = random.randint(1000,9999)
        num = int(input("Try guessing the number now "))
        while(int(num) != numbero):
            if(int(num) < int(numbero)):
                print("Little hint, the number is higher than your previews attempt")
            else:
                print("Little hint, the number is lower than your previews attempt")
            num = input("Try again!")
            tentativi += 1
        print("You did it!!!" + "\n" + "Number of attempts: " + str(tentativi) + "\n")
    elif(s == 5):
        print("You have choosen level: ⓜⓐⓓⓝⓔⓢⓢ")
        numbero = random.randint(10000,99999)
        num = int(input("Try guessing the number now "))
        while(int(num) != numbero):
            if(int(num) < int(numbero)):
                print("Little hint, the number is higher than your previews attempt")
            else:
                print("Little hint, the number is lower than your previews attempt")
            num = input("Try again!")
            tentativi += 1
        print("You did it!!!" + "\n" + "Number of attempts: " + str(tentativi) + "\n")
    else:
        print("The level you have choosen is not available")

# Manca completamente la parte della classifica!

# Il codice e' scritto benino, ma e' incompleto con tante parti che
# si potevano risparmiare usando meglio gli if. Inoltre mancano del
# tutto i commenti che sono sempre un aiuto a capire meglio il
# codice (immagina un programma di 1000 anziche' 100 righe!)