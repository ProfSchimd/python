from curses import raw
import sys

numero = int(sys.argv[1])
if numero < 0:
    print("negativo")
elif  numero == 0:
    print("nullo")
else:
    print("positivo")
