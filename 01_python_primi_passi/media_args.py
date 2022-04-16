import sys

def main():
	# Ricorda: sys.argv è una lista di stringhe
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	c = float(sys.argv[3])
	# operazioni aritmetiche 'standard'
	media = (a + b + c) / 3
	print(media)

if __name__ == "__main__":
	main()
