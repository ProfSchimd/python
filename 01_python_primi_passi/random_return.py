import random
def tipoRitornoIndeterminato():
    if (random.random() < 0.5):
        return 3.33
    else:
        return "Hello"

valore = tipoRitornoIndeterminato()
print(valore, type(valore))
