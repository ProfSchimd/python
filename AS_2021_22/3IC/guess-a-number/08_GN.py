# A cosa serve tutta questa roba che non mi fa
# eseguire il programma!!!!
# (Domanda retorica, so benissimo perche' hai tutti questi import!)
# Purtroppo tu non hai usato la sintassi corretta
# True, False, None etc
# e quindi hai importato cose 'a caso' come ti ha suggerito la IDE
# ma questo è un errore di sintassi!
from ast import Num
from asyncio.windows_events import NULL

from pickle import FALSE, TRUE
import random
from warnings import catch_warnings
#print("+---------------------------+")
#print("| Welcome to Guess a Number |")
#print("+---------------------------+")

print("  ________                                               _______               ___.                 ")
print(" /  _____/ __ __   ____   ______ ______   _____ ___.__.  \      \  __ __  _____\_ |__   ___________ ")
print("/   \  ___|  |  \_/ __ \ /  ___//  ___/  /     <   |  |  /   |   \|  |  \/     \| __ \_/ __ \_  __ \ ")
print("\    \_\  \  |  /\  ___/ \___ \ \___ \  |  Y Y  \___  | /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/")
print(" \______  /____/  \___  >____  >____  > |__|_|  / ____| \____|__  /____/|__|_|  /___  /\___  >__|   ")
print("        \/            \/     \/     \/        \/\/              \/            \/    \/     \/       ")
num_gioc=input("inserisci il numero di giocatori che parteciperanno: ")
s1=FALSE
while(s1==FALSE):
              try:
                   print(int(num_gioc))
                   s1=TRUE
              except:
                   print("inserisci un numero: ")
                   num_gioc=input()
cont=0
nome_giocatori=[]
tentativi_giocatori=[]

nomi_giocatori_1=[]
classifica_giocatori_1=[]
tentativi_giocatori_1=[]
classifica_tentativi_1=[]

nomi_giocatori_2=[]
classifica_giocatori_2=[]
tentativi_giocatori_2=[]
classifica_tentativi_2=[]

nomi_giocatori_3=[]
classifica_giocatori_3=[]
tentativi_giocatori_3=[]
classifica_tentativi_3=[]

nomi_giocatori_4=[]
classifica_giocatori_4=[]
tentativi_giocatori_4=[]
classifica_tentativi_4=[]

nomi_giocatori_5=[]
classifica_giocatori_5=[]
tentativi_giocatori_5=[]
classifica_tentativi_5=[]

difficolta_scelte=[]

def ordina(tentativi_giocatori,classifica_tentativi,nomi_giocatori):
     
     x=0
     z=0
     i=0
     classifica_giocatori=nomi_giocatori
     while int(i)<int(len(classifica_giocatori)):

             try:
               x = tentativi_giocatori.index(classifica_tentativi[z])
             except:
               x = -1
             if(int(x) != -1):
                    tentativi_giocatori[x] = NULL
                    classifica_giocatori.append(nome_giocatori[x])
                    x=0
             z+=1      
             i+=1         
     return classifica_giocatori

livelli=["Pivello","Principiante","Professionista","Gran Maestro","Leggenda"]

while(int(cont)<int(num_gioc)):
         name=input("Inserisci il tuo nickname:")
         nome_giocatori.append(name)
        
         for i in range(len(livelli)):
                print(livelli[i]," == ",i+1)
         livello=input("Seleziona il livello di difficoltà ")
         casuale=0
         s1=FALSE
         while(s1==FALSE):
              try:
                   print(int(livello))
                   s1=TRUE
              except:
                   print("inserisci un numero: ")
                   livello=input()
          # Potevi usare le potenze!
         if int(livello)==1:
              casuale=random.randint(0,9)
              nomi_giocatori_1.append(name)
         elif int(livello)==2:
              casuale=random.randint(10,99)
              nomi_giocatori_2.append(name)
         elif int(livello)==3:
              casuale=random.randint(100,999)
              nomi_giocatori_3.append(name)
         elif int(livello)==4:
              casuale=random.randint(1000,9999)
              nomi_giocatori_4.append(name)
         elif int(livello)==5:
              casuale=random.randint(10000,999999) 
              nomi_giocatori_5.append(name)
       
         difficolta_scelte.append(livello)
         print("livello selezionato ",": ",livello)
         tentativi=0
         prova=0
       
         vittoria={}
         sconfitta={}

  

         vittoria[0]= "wow hai vinto in pochi tentativi"
         sconfitta[0]="riprova con un numero maggiore"
         sconfitta[1]="riprova con un numero minore"
         while(prova!='q'):
              tentativi+=1
              print("Tentativo ", tentativi)
              prova=input("indovina il mio numero: ")
              s1=FALSE
              while(s1==FALSE):
                   try:
                      print(int(prova))
                      s1=TRUE
                   except:
                      print("inserisci un numero: ")
                      prova=input()

              if(int(prova)==int(casuale)):
                   print("Hai indovinato in ",tentativi," tentativi!")
                   if int(livello)==1:
                        tentativi_giocatori_1.append(tentativi)
                        classifica_tentativi_1.append(tentativi)
            
                   elif int(livello)==2:
                        tentativi_giocatori_2.append(tentativi)
                        classifica_tentativi_2.append(tentativi)
                   elif int(livello)==3:
                        tentativi_giocatori_3.append(tentativi)
                        classifica_tentativi_3.append(tentativi)
                   elif int(livello)==4:
                        tentativi_giocatori_4.append(tentativi)
                        classifica_tentativi_4.append(tentativi)
                   elif int(livello)==5:
                        tentativi_giocatori_5.append(tentativi)
                        classifica_tentativi_5.append(tentativi)

                   tentativi_giocatori.append(tentativi)
                   if(int(tentativi)<3):
                        print(vittoria[0])
                   break
              elif(int(prova)!=int(casuale)):
                   if(int(prova)<int(casuale)):
                        print("Scusa, il mio numero non è ",prova," ",sconfitta[0])
                   elif(int(prova)>int(casuale)):
                        print("Scusa, il mio numero non è ",prova," ",sconfitta[1])
         cont+=1
         


classifica_tentativi_1=sorted(classifica_tentativi_1)
classifica_tentativi_2=sorted(classifica_tentativi_2)
classifica_tentativi_3=sorted(classifica_tentativi_3)
classifica_tentativi_4=sorted(classifica_tentativi_4)
classifica_tentativi_5=sorted(classifica_tentativi_5)
classifica_giocatori_1=ordina(tentativi_giocatori_1,classifica_tentativi_1,nomi_giocatori_1)
classifica_giocatori_2=ordina(tentativi_giocatori_2,classifica_tentativi_2,nomi_giocatori_2)
classifica_giocatori_3=ordina(tentativi_giocatori_3,classifica_tentativi_3,nomi_giocatori_3)
classifica_giocatori_4=ordina(tentativi_giocatori_4,classifica_tentativi_4,nomi_giocatori_4)
classifica_giocatori_5=ordina(tentativi_giocatori_5,classifica_tentativi_5,nomi_giocatori_5)


x=0
j=0
z=0
i=0
path="Punteggio.txt"
f=open(path,"w")
f1=open(path,"r")
x=0
f.write("nome,n_tentativi,difficoltà \n")
while int(x) < int(num_gioc):
   f.write(str(nome_giocatori[x]))
   f.write(";")
   f.write(str(tentativi_giocatori[x]))
   f.write(";")
   f.write(str(difficolta_scelte[x]))
   f.write("\n")
   x+=1

x=0

def scoreboard(n):
     print("***************************")
     print("*      Scoreboard"," ","(",n,")","*")
     print("***************************")
     print("+-------------------------+")
     print("***************************")
     print("|  Pos   Name   Attempts  |")
     print("+-------------------------+")

def stampa_dei_giocatori(classifica_giocatori,classifica_tentativi):
     z=0
     j=1
     while int(z) < int((len(classifica_giocatori)/2)):
          lun=len(classifica_giocatori[x])
          if int(lun)<4:
               print("|  ",j,"\t",classifica_giocatori[z],"\t",classifica_tentativi[z],"\t ","|")
          else:
               print("|  ",j,"\t",classifica_giocatori[z][0],"...","\t",classifica_tentativi[z],"\t ","|")
          j+=1
          z+=1
          print("+-------------------------+")

def classifiche1():
     x=0
     m=0
     a=0
     r=0
     i=0
     o=0
     
     while int (x)< int(num_gioc):
          # Sarebbe stato meglio pensare di usare un codice un pi' piu'
          # corto cercando di mettere dentro gli if e elif solo le cose
          # che cambiano veramente tra un livello di difficolta' ed un
          # altro.
          if int(difficolta_scelte[x])==1 and  int(m)!=1:
               scoreboard(1)
               
               stampa_dei_giocatori(classifica_giocatori_1,classifica_tentativi_1)
               
               m=1
               print()
               print()
          elif int(difficolta_scelte[x])==2 and int(a) != 1:
               scoreboard(2)
               
               stampa_dei_giocatori(classifica_giocatori_2,classifica_tentativi_2)
               a = 1
               print()
               print()
          elif int(difficolta_scelte[x])==3 and int(r)!=1 :
               scoreboard(3)
               
               stampa_dei_giocatori(classifica_giocatori_3,classifica_tentativi_3)
               r = 1
               print()
               print()
          elif int (difficolta_scelte[x])==4 and int(i)!=1:
               scoreboard(4)
               
               stampa_dei_giocatori(classifica_giocatori_4,classifica_tentativi_4)
               
               i = 1
               print()
               print()
          elif int(difficolta_scelte[x])==5 and int(o)!=1:
               scoreboard(5)
               
               stampa_dei_giocatori(classifica_giocatori_5,classifica_tentativi_5)
               
               o = 1
               print()
               print()
               
          x+=1

classifiche1()
f.close()
f1.close()

# In generale il programma è fatto benino, ma ci sono cose da migliorare
# sopratutto l'uso dei commenti ed il nome delle variabili che non sono
# un grosso problema (ma piccolo) in un programma di 300 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti e nomi di
# variabili scelti bene.


