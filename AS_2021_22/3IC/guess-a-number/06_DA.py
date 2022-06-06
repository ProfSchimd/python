import random

# potevi usare la potenza 'math.pow' 10^1 - 1, 10^2 - 1, ...
# per esercizio ti suggerisco di provare a modificare il codice
def randomn(number):
    
    if(number == 1):
        rn=random.randint(1,9)
    elif(number == 2):
        rn=random.randint(10,99)
    elif(number == 3):
        rn=random.randint(100,999)
    elif(number == 4):
        rn=random.randint(1000,9999)
    elif(number == 5):
        rn=random.randint(10000,99999)
    else:
        print("No available")
    return rn    

def lt(string):
    tup=(string)
    return tup
    
            
    
        
game = "Guess a Number"
print("Welcome to "+game)
print("Please, type your nickname :")
nickname = input()
print("Hello "+nickname)
print("Choose the difficulty between 1-5")
d=input()


try :
    
    dif=int(d)
    
    
except:
    
    print("the difficult level "+d +" is not available")
    
    

randomnumber= randomn(dif)
condition = True
condtion2=True
count=0

while(condition):
    count=count+1
    print("Attemps"+str(count))
    print("Guess the number" + " "+nickname)
    n=input()
    if(n=="q"):
        condition= False
        condtion2=False
        
    nu= int(n)
    # mi permetto di dire che devi lavorare mooooolto sull'inglese
    if(nu==randomnumber):
        print("---------------------------------------------"+"\n")
        print("Congratulations you have find the segret number: "+ str(randomnumber)+ " in "+ str(count) + " attemps")
        condition= False
        
    elif(nu > randomnumber):
        print("---------------------------------------------"+"\n")
        print("your number is more bigger than segret number"+ "\n" )
        
    elif(nu<randomnumber):
        print("---------------------------------------------"+"\n")
        print("your number is more littler than segret number"+"\n")
        
file ="classifica.txt"        
        
if(condtion2):
    o= open(file,"a")
    o.write(nickname+","+str(count)+","+str(dif)+"\n")
    o.close()
    
o = open(file,"r")  
for riga in o:
    line=riga.rstrip('\n')
    t= lt(line.split(","))
# questo mostra sempre e solo l'ultima riga, oltretutto
# lo mostra in un modo poco 'user friedly', vale a dire
# mostra una lista Python (non proprio la cosa più bella
# da vedere)
print(t)

# Il programma è incompleto e fatto male, mancano completamente
# dei commenti che è un grosso problema (ma piccolo) in un programma di 150 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti.

