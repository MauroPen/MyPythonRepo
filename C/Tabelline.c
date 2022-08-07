#include <stdio.h>

int main () {
	int tab, lungh, ris;
	int i;                                          //Contatore
	
	printf ("Generatore di tabelline.\n\nInserire il numero di cui si vuole conoscere la tabellina.\n");
	scanf ("%d", &tab);

	while (tab <= 0) {
	printf ("\nInserire un numero intero positivo\n");
	scanf ("%d", &tab);
}   

    printf ("\nInserire la lunghezza della tabellina desiderata.\n");
    scanf ("%d", &lungh);
    
	while (lungh <= 0) {
	printf ("\nInserire un numero intero positivo\n");
	scanf ("%d", &lungh);
}

for (i = 1; i <= lungh; i++) {
	ris = tab * i;
	printf ("%d ", ris);
}

return 0;	
}
