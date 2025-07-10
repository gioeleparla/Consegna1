
def perimetro():
print("Calcolo del perimetro di una figura geometrica a tua scelta")
print("Quadrato")
print("Cerchio")
print("Rettangolo")

print("Di quale figura vuoi calcolare il perimetro? ")
scelta = int(input("Inserisci la scelta: "))
if scelta = Quadrato:
print("Hai selezionato il perimetro del quadrato")
lato = float(input("Inserisci la lunghezza del lato del quadrato "))
print("Il perimetro del Quadrato avendo un lato di", lato, "è:", lato *4)
elif scelta = Cerchio:
print("Hai selezionato il perimetro del cerchio")
raggio = float(input("Inserisci il valore del raggio del cerchio "))
print("Il perimetro del Cerchio com un raggio di", raggio, "è:", 2* raggio* 3.14)
elif scelta = Rettangolo:
print("Hai selezionato il perimetro del rettangolo")
base = float(input("Inserisci il valore della base del rettangolo "))
print("Il perimetro del Rettangolo com una base di", base, "e altezza", altezza, "è:" , base*2 + 2*altezza)
else:
print ("inserire una scelta valida")

perimetro()

  


