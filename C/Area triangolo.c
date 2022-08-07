#include <stdio.h>

int main () {
	int base, altezza;
	float area;                                                                 //L'area potrebbe essere decimale
	
	printf ("Calcolo area di un triangolo qualunque\n\nImmettere il valore della base e dell'altezza\n");
	scanf ("%d %d", &base, &altezza);
	
	while (base<=0 || altezza<=0) {                                             //Condizioni di esistenza, ciclo dipendente dall'utente
		printf ("Immettere valori maggiori di 0\n");
		scanf ("%d %d", &base, &altezza);
	}
	area = (float) (base * altezza) / 2;   
	                                     
	printf ("L'area del triangolo di base %d e altezza %d � %f\n", base, altezza, area);
	return 0;
}
