import random

# non hai definito nessuna funzione, di solito è meglio
# farlo per dividere le parti del programma.

# non ci sono commenti e le variabili non hanno nomi
# che speigano bene cosa contengono, quindi è difficile
# capire il tuo programma

a=0
num=0
tent=0
nome=""
print("Benvenuto al gioco casuale di numeri. \nDovrai indovinare in meno tentativi il numero che sto pensando!")
nome=input("Intanto, perché non mi dici il tuo nome: ")
print("bene " + nome)
while True:
    try:
        a=input("\nper cominciare a giocare mi dica il livello di difficoltà(da 1 a 5): ")
        int(a)
        print("hai selezionato la difficoltà: " + str(a))
    except:
        print("difficoltà non valida")
        continue
    break
# ti viene in mente un modo usando le potenze di 10?
if(int(a)==1):
    num=random.randint(0,9)
elif(int(a)==2):
    num=random.randint(0,99)
elif(int(a)==3):
    num=random.randint(0,999)
elif(int(a)==4):
    num=random.randint(0,9999)
elif(int(a)==5):
    num=random.randint(0,99999)
while True:
    try:
        risp=-1
        while(int(risp)!=num):
            risp=input("prova ad indovinare il numero: ")
            tent+=1
            if(int(risp)==num):
                print("numero corretto! ci hai messo: " + str(tent) + " tentativi!")
                # si poteva usare un unico file
                if (a==1):
                    f1 = open("classifica1.txt", "a")
                    f1.write(nome+str(tent)+"\n")
                    f1.close()
                    # questo non legge nulla perche' f1 e' stato chiuso
                    for riga in f1:
                        print(riga)
                elif (a==2):
                    f2 = open("classifica2.txt", "a")
                    f2.write(nome+str(tent)+"\n")
                    f2.close()
                    for riga in f2:
                        print(riga)
                elif (a==3):
                    f3 = open("classifica3.txt", "a")
                    f3.write(nome+str(tent)+"\n")
                    f3.close()
                    for riga in f3:
                        print(riga)
                elif (a==4):
                    f4 = open("classifica4.txt", "a")
                    f4.write(nome+str(tent)+"\n")
                    f4.close()
                    for riga in f4:
                        print(riga)
                elif (a==5):
                    f5 = open("classifica5.txt", "a")
                    f5.write(nome+str(tent)+"\n")
                    f5.close()
                    for riga in f5:
                        print(riga)
            else:
                print("numero sbagliato! riprova!")
                if(int(risp)<num):
                    print("più in alto")
                else:
                    print("più basso")
    except:
        print("numero non valido")
        continue
    break

# La classifica non viene mai mostrata sullo schermo

