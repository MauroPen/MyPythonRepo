#include <stdio.h>

float media (int, int);

int main () {
	int val, somma = 0, i = 0, stop = 0;                                    //Contatore tiene traccia del numero dei valori inseriti
	
	printf ("Calcolo media valori\n\nInserire valore\n");
	scanf ("%d", &val);  
	                                                     
	while (val != stop) {                                                   //Ciclo dipendente da utente
	
		while (val < 0) {                                                   //Condizione di esistenza del valore
			printf ("Inserire valore valido\n");
			scanf ("%d", &val);
		};
	
	somma += val;                                                           //Somma valori inseriti
	i++;
	printf ("\nInserire valore o terminare con 0\n");
	scanf ("%d", &val);
	}

if (i == 0)                                               					//Un solo valore inserito
	i = 1;
	
printf ("\nLa media dei valori � %f", media (somma, i));
return 0;
}


float media (int x, int y) {
	int risultato;
	risultato = (float) x/y;
	return risultato;
}
