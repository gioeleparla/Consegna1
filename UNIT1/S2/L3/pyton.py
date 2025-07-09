n  = 0

while n < 10:
    print(n)
    n=n+1

    exit 

#variabili 
    marta = 0 
    marta = 1

    marta_prima=1 
    #le variabili per convenzione sono snake_case e differenzia 
    # da Marta a marta 

# intero
    x=10
#virgola mobile
y=3.14
# stringa 
nome="Alice"
# la stringa in fase di dichiarazione può avere diversi formati basta 
# anteporre una lettera prima delle virgolette, se la metto abilito la possibilità
#di inserire funzioni  o variabili
nome=f"Alice {y}"
print(nome) #Alice 3.14

#true/false
utente_attivo=True
#lista
numeri = [1,2,3,4]
# tuple
coordinate = (10,20)
# dizionari
utente = {"nome", "alice" , "eta": 25}

x = x + y 
print(x)

#STRINGE
x = "Hello, World"
print(x.split(sep=",")) # "Hello" , "World"
print(x.upper())  # HELLO, WORLD
# il primo te lo separa il secondo tutto in maiuscolo 
y = "this is python"

print(x + " " +y) # Hello, World this is Python perchè unisce le 2 stringhe

vett=x.split(sep=",")
print(vett[0]+vett(1).strip()) #stampa HelloWorld
#si accede alla stringhe utilizzando l'operatore . prima del metodo

#INPUT

x = input ("inserisci una stringa: ")
print(x) #stammperà quello che abbiamo scritto 
print(x.upper())  #stamperà linput ma tutto maiuscolo 

#if else e controllo di flusso 

x = 10 
y = 20 

if x < y:    
    print("x è minore di y") #eeuito se è vera 
else:    
    print("x è maggiore o uguale a y") #eseguita se falsa 
#stamperà x è minore di y

x = int(input("inserisci un numero: "))
#il cast per numero intero è int 
if x < 10:
    print("il numero inserito è minore di 10")
else:
    print("il numero inserito è maggiore o uguale a 10")
# stamperà che inserisci tu un numero e ti dirà se è minore o uguale ecc

#se facciamo elif al posti di else 

elif (x==10):
print("il numero inserito è uguale a 10")
else:
print("il numero inserito è maggiore a 10)")
#esempio 
x = 10 
y = 20 
z = 30 
if x > y:    
    print("x è maggiore di y") 
elif y > z:    
    print("y è maggiore di z") 
elif x < z:    
    print("x è minore di z") 
else:    
    print("Nessuna delle condizioni precedenti è vera")

#while blocco codice ripetuto finchè non è vero

i = 0 
while i < 5    
    print("i è: ", i)    
    i += 1
# printerà i è 0 
# i è 1 
# iè 2 
# iè 3 ecc 

# for blocco di codice eseguito per ciascun valore nella sequenza

numeri = 1, 2, 3, 4, 5 
for numero in numeri:    
    print("Numero: ", numero)

    #quando passerà dal print numero stamerò al primo valore e cosi via 
    # for supporta funziona range() che funziona che stampa in modo più flessibile
x=10

for i in range(2, x, 4): # range(x)
    print("i" , i)
    #stamperà 1: 0 1:2 1:3 
    # start stop step  puoi decidere che numeri resittuire dove fermarsi ecc

#lista 
lista = [1, "ciao", 3.14, 1, 2, 3]
print(lista[0  # Stampa: 1 
print(lista[1  # Stampa: ciao 
print(lista[2  # Stampa: 3.14 
print(lista[3  # Stampa: 1, 2, 3 
print(lista[30])  # Stampa: 1 (accesso al primo elemento della lista interna)

lista.pop() #rimuove l'ultimo elemento
lista.remove(ciao) #ha rimosso ciao o elemento specifico

#list.append() mette un elemento alla fine 
lista.append([1,2,3,6]) #
printi(lista) #ha aggiunto questo elemento
##lista.insert(elemento da dopo quale inserire, elemento nuovo)
lista.insert(0."ciao")
#l'ha messo dopo 0 il ciao 

#rimuovere elementi per posizione usiamo del lista 
del lista[2]

#aostituire un elemento della lista 
lista[0] = "Franco" #0 sostiutisco con franco 

#DIZIONARI

# i dizionari è fatto per strutturare i dati e devi usare i vaolri e chiave 
dizionario ={
    "nome":"alice", #nome sono le chiavi e alice sono i valori associati a quelle chiavi
}

dizionario = {   
     "nome": "Alice",    
     "età": 30,   
     "città": "Roma"
 }

 print(dizionario["nome"])  # Stampa: Alice 
 print(dizionario["età"])   # Stampa: 30 
 print(dizionario["città"]) # Stampa: Roma

 #si può modificare l'età di alice 
 dizionario["età"] = 31 
 print(dizionario)

 #aggiungere anche elemento 
 dizionario [email] = "ccccc@gmail.com"
 print(dizionario)
 #stamperà alice 31 roma e mail 

 #per rimuovere un elemento utilizziamo pop o del (del dizionario["email"])
 dizionario.pop("città") #stamperà tutto senza roma 

#● Dizionario [«chiave»]: restituisce il valore relativo alla chiave specificata. 
# ● Dizionario.values(): scrive a schermo tutte i valori delle chiavi contenute nel dizionario. 
# ● Dizionario.keys(): scrive a schermo tutte le chiavi presenti nel dizionario. 
# ● Aggiungo una nuova coppia chiave:valore utilizzando la sintassi dizionario [«nuova_chiave»] = «nuovo valore».

print(dizionario.keys()) #stampa nome età 
print(dizionario.values()) #stamp alice 31
print(dizionario.items()) #nome alice, età 31 serve per prendere le coppie con for


#FUNZIONI 
#utili per organizzare il codice in blocchi logici 
# ● def: indica che si sta definendo una funzione. Cyber Security & Ethical Hacking Introduzione alle funzioni 
# ● function_name: è il nome che si vuole dare alla funzione, che sarà poi utilizzato allʼinterno del programma per richiamare quella parte di codice. 
# ● parameter: è la lista di parametri che la funzione accetta. I parametri sono opzionali. 
# ● istruzioni: questa sezione contiene il blocco di codice che verrà eseguito quando la funzione verrà richiamata allʼinterno del programma. 
# ● return: questa istruzione esce dalla funzione e passa lʼesecuzione del programma alla funzione chiamante, restituendo eventualmente un valore.

def saluta(nome): #indico cosa deve fare 
saluto=f"Ciao {nome}!" #oppure saluto = "ciao" + nome + "!"
return saluto

nome = input("ciao come ti chiami) ")
messaggio = saluta(nome)
print(messaggio)
#stampa: inserisci ilnome dopo il come ti chiami e lui ti saluta 

def somma(a, b):
risultato = a + b
return (risultato)
print(somma(3,5)) #stamperà 8 

# Definizione di una funzione senza parametri 
# def saluto_generale():    
# return "Ciao a tutti!" 
# 
# # Richiamo della funzione 
# print(saluto_generale())  
# # Stampa: Ciao a tutti!
#generale senza precise indicazioni 

#Quando si utilizzano le funzioni in Python,
#  è fondamentale capirne lo scope, ovvero l'ambito di utilizzo delle variabili.
#variabile locale e globale 

def saluta(nome, messaggio):
print(f"{messaggio} {nome}!")

saluta("Alice" , "Ciao")
saluta("Bob" , "Buongiorno") #stampa ciao alice! e buongiorno bob!

saluta (messaggio="ciao" , nome="Franco") #stampa ciao franco!
#perchè se do i nomi alle variabili poi posso con un = forzare le variabili anche
#se non è nella loro posizione, (opzionali)

#se mettevo messaggio="Ciao" in def
e scrivo saluta(nome="Ciro") #Ciao Ciro!
saluta("piera") #Ciao piera!







