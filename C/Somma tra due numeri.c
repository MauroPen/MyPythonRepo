#include <stdio.h>

int main () {
	int Num1, Num2;
	
	printf ("Somma tra due numeri\n\n");
	
	printf ("Inserisci il primo numero da sommare\n");
	scanf ("%d", &Num1);
	
	printf ("Inserisci il secondo numero\n");
	scanf ("%d", &Num2);
	
	printf ("La somma tra i due numeri è %d", Num1 + Num2);
	return 0;
}
