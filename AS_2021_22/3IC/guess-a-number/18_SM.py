import random


# va bene, ma c'è anche modo di farlo con un solo file
path1="Testo1.csv"
path2="Testo2.csv"
path3="Testo3.csv"
path4="Testo4.csv"
path5="Testo5.csv"
reader1=open(path1, "w")
reader2=open(path2, "w")
reader3=open(path3, "w")
reader4=open(path4, "w")
reader5=open(path5, "w")

# senza neanche un piccolo commento non si capisce niente 
# di tutto quello che stai facendo con la miriade di
# variabile che stai definendo sotto (senza contare che i
# nomi scelti non sono certo i migliori!)
i=0
lun1=0
lun2=0
lun3=0
lun4=0
lun5=0
ordine1=[" "]
ordine2=[" "]
ordine3=[" "]
ordine4=[" "]
ordine5=[" "]
tentativi1=[0]
tentativi2=[0]
tentativi3=[0]
tentativi4=[0]
tentativi5=[0]
difficoltà=["Pivello","Principiante","Apprendista","Maestro","Gran Maestro"]
scelta=int(input("Dimmi il numero di giocatori: "))

#ordine delle classifiche
def stampaClassifica(livello,ordine,tentativi, reader):
    l=0
    j=0
    appo=0
    appoggio=" "
    while j<ordine.len-1:
        while l<ordine.len-1:
            if tentativi[j]<tentativi[l]:
                appo=tentativi[j]
                tentativi[j]=tentativi[l]
                tentativi[l]=appo
                
                appoggio=ordine[j]
                ordine[j]=ordine[l]
                ordine[l]=appoggio
    l=1
    reader.write("***************************")
    reader.write("*    Scoreboard(",livello,")    *")
    reader.write("***************************")
    reader.write("+-------------------------+")
    reader.write("| Pos  Name      Attempts |")
    reader.write("+-------------------------+")
    while(l<ordine.len):
        reader.write("| ",l,"\t",ordine[l-1],"\t",tentativi[l-1],"\t\t |")
        l=l+1
    reader.write("+-------------------------+")
    
    
    
#corpo principale del programma
while i <scelta:
    print("+---------------------------+")
    print("| Welcome to Guess a number |")
    print("+---------------------------+")
    print()
    nome = input("Pls type ur nickname: ")
    print("Hi",nome,"! let's play togheter")
    livello = int(input("Seleziona il livello di difficoltà 1-5: "))
    if(livello>5  or livello<1):
        while livello>5  or livello<1:
            print("Hai sbagliato ad inserire la difficoltà del livello, reinserisci ")
            livello = int(input("Seleziona il livello di difficoltà 1-5: "))
    print("Livello: ",livello," -->",difficoltà[livello-1])
    #verifico il livello e genero il numero incognito

    # potevi usare la potenza 'math.pow' 10^1 - 1, 10^2 - 1, ...
    # per esercizio ti suggerisco di provare a modificare il codice
    if (livello == 1):
        num = random.randint(0,9)
        print("Indovina il numero tra 0 e 9 ")
        ordine1.append(nome)
        lun1=lun1+1
    elif (livello == 2):
        ordine2.append(nome)
        lun2=lun2+1
        num = random.randint(10,99)
        print("Indovina il numero tra 10 e 99 " )
    elif (livello == 3):
        ordine3.append(nome)
        lun3=lun3+1
        num = random.randint(100,999)
        print("Indovina il numero tra 100 e 999 " )
    elif (livello == 4):
        ordine4.append(nome)
        lun4=lun4+1
        num = random.randint(1000,9999)
        print("Indovina il numero tra 1000 e 9999 " )
    elif (livello == 5):
        ordine5.append(nome)
        lun5=lun5+1
        num = random.randint(10000,99999)
        print("Indovina il numero tra 10000 e 99999 ")
    condizione = True
    cont=1
    #calcolo i tentativi fatti dall'utente

    # Questa parte è identica a quella di un tuo compagno
    # non serve nemmeno che ti dica chi!
    while(condizione):
        print("Tentativo ",cont)
        attempt = int(input( " guess my number: "))
        if(attempt<num):
            print("Sbagliato, prova un valore più alto ")
        elif(attempt==num):
            print("Bravo hai indovinato dopo ",cont," tentativi!")
            condizione=False
        elif(attempt>num):
            print("Sbagliato, prova un valore più basso")
        cont=cont+1
        #se l'utente si stufa può uscire dal game
        if(cont>15):
            print("Vuoi arrenderti?")
            arrandersi = input("Scrivi Si o NO ")
            if(arrandersi=="Si"):
                print("Il valore corretto era ",num)
                condizione=False
                cont=1000
                
    if(livello==1):
        tentativi1.append(cont)
    elif(livello==2):
        tentativi2.append(cont)
    elif(livello==3):
        tentativi3.append(cont)
    elif(livello==4):
        tentativi4.append(cont)
    elif(livello==5):
        tentativi5.append(cont)
    i=i+1        


# era meglio stampare solo la classifica del livello a cui
# si era scelto di giocare.
# Peccato solo che il codice sotto dia errore, ma l'hai
# provato almeno?   !!

#stampo le classifiche        
stampaClassifiche(1,ordine1,tentativi1,reader1)
stampaClassifiche(2,ordine2,tentativi2,reader2)
stampaClassifiche(3,ordine3,tentativi3,reader3)
stampaClassifiche(4,ordine4,tentativi4,reader4)
stampaClassifiche(5,ordine5,tentativi5,reader5)
reader1.close()
reader2.close()
reader3.close()
reader4.close()
reader5.close()

# Il codice è scritto in modo abbastanza confuso, non funziona 
# perché stampa sempre una classifica vuota e alla fine dà
# anche errore sulle ultime righe (il motivo è ovvio una volta
# che si vede il messaggio di errore). Sono abbastanza sicuro
# che non hai per niente provato il tuo codice!

# Errore 

# Sbagliato, prova un valore più basso
# Tentativo  4
#  guess my number: 8
# Bravo hai indovinato dopo  4  tentativi!
# Traceback (most recent call last):
#   File "18_SM.py", line 149, in <module>
#     stampaClassifiche(1,ordine1,tentativi1,reader1)
