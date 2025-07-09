#include <stdio.h>
int main() {
    int numero1, numero2; //numeri inseriti interi 
    int prodotto; //variabile per il prodotto

    printf("Calcoliamo la moltiplicazione tra 2 numeri.\n");

    printf("inserisci il primo numero: ");
    scanf("%d", &numero1); //per far inserire il primo numero

    printf("inserisci il secondo numero: ");
    scanf("%d", &numero2); //per far inserire il secondo numero

    prodotto = numero1 * numero2; //per calcolare il prodotto tra i 2 numeri

    printf("Il prodotto dei due numeri è: %d\n" , prodotto);

return 0;
}