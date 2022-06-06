import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene dichiarare varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

print('+---------------------------+')
print('| Welcome to Guess a Number |')
print('+---------------------------+')

c=0
nickname = input('Please, type your nickname: ')
print('Hi ' + nickname + '! Let"s play together')

difficolta = input('Che livello di difficoltà?')
print('Hai scelto la difficoltà ' + difficolta + ' !')
# Potevi usare le potenze! 
if ((int(difficolta)) == 1):
    num = random.randint(0,10)
elif ((int(difficolta)) == 2):
    num = random.randint(10,99)
elif ((int(difficolta)) == 3):
    num = random.randint(100,999)
elif ((int(difficolta)) == 4):
    num = random.randint(1000,9999)
elif((int(difficolta)) == 5):
    num = random.randint(10000,99999)

print(num) ## Vedo il numero da indovinare!!!
while True:
    c+=1
    input = int(input('Enter Number: '))
    if(input<num):
        print("attempt" + (str(c)) + "!")
        print( nickname+"  guess number" )
        print(input)
        print('Try a bigger number')
        continue
    elif(input>num):
        print("attempt" + (str(c)) + "!")
        print(nickname + "  guess number")
        print(input)
        print('Try a smaller number')
        continue
    else:
        print("attempt" + (str(c)) + "!")
        print(nickname +"  guess number")
        print(input)
        print('You won after  '+ (str(c))+ 'attempts')

# Mi hai mandato una versione vecchia in cui c'e' ancora
# il problema sotto che avevamo (mi pare) risolto insieme

# Traceback (most recent call last):
#   File "04_DK.py", line 28, in <module>
#     input = int(input('Enter Number: '))
# TypeError: 'int' object is not callable

# Ci sono altre cose da migliorare
# sopratutto l'uso dei commenti ed il nome delle variabili che non sono
# un grosso problema (ma piccolo) in un programma di 50 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti e nomi di
# variabili scelti bene.