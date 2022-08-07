#include <stdio.h>

#define N 100 					//Arbitrario

int max (int []);				//Basta il vettore

int main () {
	int arr[N], i = 0, mass;
	
	printf ("Calcolo valore massimo di un array.\n\nInserire uno alla volta i valori da valutare. (0 per terminare)\n", N);
	
	do {
		scanf ("%d", &arr[i]);
		i++;
	} while (arr[i-1] != 0 && i < N+1);
	
	mass = max (&arr[0]);
	
	printf ("\n\nIl massimo valore e' %d.", mass);
	
	return 0;
}

int max (int arr[]) {
	
	if (arr[0] == 0) return 0;
	
	if (arr[0] >= max (&arr[1])) return arr[0];
	
	else return max (&arr[1]);
}
