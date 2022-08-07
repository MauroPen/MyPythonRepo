#include <stdio.h>

int main () {
	int num1, num2, min;
	int i;                            //Contatore divisori
	
	printf ("Calcolo divisori comuni di due numeri.\n\nInserisci il primo numero.\n");
	scanf ("%d", &num1);
	while (num1 <= 0) {
		printf ("\nInserisci un numero intero positivo!\n");
		scanf ("%d", &num1);
	}
	
	printf ("\nInserisci il secondo numero.\n");
	scanf ("%d", &num2);
	while (num2 <= 0 || num2 == num1) {
		printf ("\nInserisci un numero intero positivo diverso dal primo!\n");
		scanf ("%d", &num2);
	}
	
	if (num1 < num2) {                  //Assegnazione minimo
		min = num1;
}   else min = num2;

printf ("\nI divisori comuni ai due numeri sono: ");

for (i = 1; i <= min; i++) {
	if (num1 % i == 0 && num2 % i == 0) {
		printf ("%d ", i);
		}
	} return 0;
}
