import math
import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene dichiarare varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

tentativi = 0
numeroinp = 0
test = False
tuplelist=[]

Nomi = ["Pivello","Principiante","Addestrato","Genio","GranMaestro"]
print ("Welcome to Guess the Number!!")
name = input("Type your nickname: ")
print ("Let's start to play "+ name+"!!")
while True:
  try:
    difficulty = int(input("Select a difficulty between 1 and 5: "))
    break
  except:
    print("Input error")
    difficulty=-1
print("Difficulty: "+Nomi[difficulty-1])
path= "classifica"+str(difficulty)+".txt"
f = open(path, "a")
while (difficulty < 0) or (difficulty > 5):
  try:
    difficulty = int(input("Difficulty must be 1,2,3,4 or 5: "))
  except:
    print("Input error")
    difficulty=-1
# Molto bene!
numero = random.randint(math.pow(10,(difficulty-1)),math.pow(10,(difficulty))-1)
# Ooooops! si vede la soluzione :)
print(numero)

while(numeroinp!=numero):
  try:
    if(tentativi==0):
      numeroinp = int(input("Try and guess the number: "))
    else:
      numeroinp = int(input("Try again: "))
    tentativi+=1
    test=False
  except:
    print("Input error")
    test=True
  if (numeroinp>numero and test == False):
    print("Too high!")
  elif(numeroinp<numero and test == False):
    print("Too low!")
print("Well done! You guessed it right!")
print(tentativi)
f.write(name+":"+str(tentativi)+"\n")
f.close()

# La classifica non viene mai mostrata a schermo!

# In generale il programma è fatto bene, ci sono alcune cose da migliorare
# sopratutto l'uso dei commenti che non è un grosso problema in un programma
# di 60 righe, ma vale la pena abiutarsi ad usarli sempre.



