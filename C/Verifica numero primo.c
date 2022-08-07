#include <stdio.h>

int verificaPrimo (int);


int main () {
	int num;
	
	printf ("Numero primo?\n\nInserire il numero da valutare.\n");
	scanf ("%d", &num);
	
	if (verificaPrimo (num) == 1) {
		printf ("\n%d non e' primo!", num);
		return 1;
	}
	else printf ("\n%d e' primo", num);
   return 0;	
}

int verificaPrimo (int num) {
	int i;
	for (i = num-1; i > 1; i--) {
		if (num % i == 0)
			return 1;
		}
	return 0;
}
