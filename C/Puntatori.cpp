#include <stdio.h>

typedef int *punt;              		//solo per x, perchè int

typedef struct {
	int civico;
	char via[666];
} casa;

int main () {
	int x = 3, y[]={5,9};
	casa a, *pu = &a;                   //Variabile puntatore del tipo casa inizializzata a puntare ad a

 	punt p=&x, q=y;
	
	pu->civico = 12;
	
	printf ("Il civico è %d\n", a.civico);
	printf ("Puntatore dereferenziato: %d\n", *p);
	printf ("Valore puntatore: %d\n", p);
	printf ("Indirizzo di x: %d\n", &x);
	printf ("Valore di x: %d\n", x);
	printf ("Valore di y[0]: %d\n", *q);
	printf ("Valore di y[1]: %d\n", *(q+1));
	printf ("Indirizzo di y: %d\n", q);
	printf ("Distanza tra x e y: %d\n", p-q);
}
