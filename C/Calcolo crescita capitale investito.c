#include <stdio.h>

#define TASSO_INTERESSE 10             //Scelto arbitrariamente

int main () {
	int capitale, anni, i, scelta = 0;
	
	do {
	printf ("\nCalcolo crescita capitale investito.\n\nInserire il capitale iniziale.\n");
	scanf ("%d", &capitale);
	printf ("\nOra inserire il numero di anni per cui si vuole investire tale capitale.\n");
	scanf ("%d", &anni);
	
	for (i = 1 ; i <= anni ; i++) {
		capitale += (capitale * TASSO_INTERESSE)/100;
		printf ("\nAlla fine del %do anno, il capitale ammonterà a %d Euro.\n", i, capitale);
	}
	printf ("\n\nVuoi riavviare il programma? (0) SI  (1) NO\n");
	scanf ("%d", &scelta);
	} while (scelta == 0);
	return 0;
}
