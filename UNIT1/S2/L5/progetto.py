import datetime

def assistente_virtuale(comando):
    if comando == "Qual è la data di oggi?":
        oggi = datetime.date.today()
        risposta = "La data di oggi è: " + oggi.strftime("%d/%m/%Y")
    elif comando == "Che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è: "+ ora_attuale.strftime("%H:%M")
    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda"
    return risposta
while True:
    comando_utente = input("Cosa vuoi sapere? ")
    if not comando_utente.strip.lower():
        print("Per favore inserisci un comando valido.")
        continue
    if comando_utente.strip.lower() == "esci":
        print ("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente))
        



