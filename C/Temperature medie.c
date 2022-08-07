#include <stdio.h>

int main () {
	float genn [31] = {2.0, 3.0, 4.0, 2.5, -9.0, -6.0, -8.0, -0.0, -4.0};      //31 valori da inizializzare in float anche neg
    float media, somma = 0.0;
    int g1, g2, div;
    
    printf ("Media temperature di gennaio.\n\nInserire il periodo di interesse inserendo il primo e l'ultimo giorno separato da spazio.\n");
    scanf ("%d %d", &g1, &g2);

	for (g1-=1; g1 <= (g2 - 1); g1++)
 	somma += genn[g1];
 	
 	div = (g2 - g1) + 1;
 	
 	media = somma / div;
 	
 	printf ("\nLa temperatura media è stata di %.2f gradi centigradi.", media);
 return 0; 
}
