def saluta(nome="anonimo", cognome=""):
    print("Hello " + nome + " " + cognome + "!")

saluta() # 'Hello anonimo!'
saluta("Mario") # 'Hello Mario!'
saluta("Mario", "Rossi") # 'Hello Mario Rossi!'
saluta(cognome="ignoto") # 'Hello anonimo ignoto!'
saluta(cognome="Verdi", nome="Andrea") # 'Hello Andrea Verdi!'