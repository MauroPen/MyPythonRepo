#include <stdio.h>
#include <strings.h>

#define N 10   //Lunghezza massima stringa, scelta arbitrariamente

int occorrenze (char*, char);

int main () {
	int ris;
	char parola [N], lettera;
	
	printf ("Numero occorrenze di una lettera in una parola.\n\nInserire la parola da analizzare (Max %d caratteri)\n\n", N);
	scanf ("%s", parola);
	
	printf ("\n\nInserire la lettera di cui cercare le occorrenze nella parola\n\n");
	scanf ("\n%c", &lettera);
	
	ris = occorrenze (&parola[0], lettera);
	
	if (ris == 0) 
		printf ("\n\nLa lettera %c non e' presente all'interno della parola %s.\n", lettera, parola);
	
	else 
		printf ("\n\nLa lettera %c e' presente %d volte all'interno della parola %s.\n", lettera, ris, parola);	
	
return 0;
}

int occorrenze (char parola [], char lettera) {
	int i = 0;
	
	if (parola [i] == '\0')
		return 0;
	
	else if (parola[i] == lettera)
		return 1 + occorrenze (&parola[i+1], lettera);
	
	else return 0 + occorrenze (&parola [i+1], lettera);
}
