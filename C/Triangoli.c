#include <stdio.h>

int main () {
	float l1, l2, l3;
	
	printf ("Analisi triangolo.\n\nInserire il primo lato del triangolo.\n");
	scanf ("%f", &l1);
	while (l1 <= 0) {
		printf ("\nInserire un intero positivo!\n");
		scanf ("%f", &l1);
	}
	
	printf ("\nInserire il secondo lato del triangolo.\n");
	scanf ("%f", &l2);
	while (l2 <= 0) {
		printf ("\nInserire un intero positivo!\n");
		scanf ("%f", &l2);
	}
		
	printf ("\nInserire il terzo lato del triangolo.\n");
	scanf ("%f", &l3);
	while (l3 <= 0) {
		printf ("\nInserire un intero positivo!\n");
		scanf ("%f", &l3);
    }
	
	//Controllo validità triangolo
	if (l1 + l2 <= l3 || l2 + l3 <= l1 || l1 + l3 <= l2) {
		printf ("\nI lati inseriti non formano un triangolo.");
		return 1;
}
    //Triangolo equilatero
    if (l1==l2 && l2==l3) {
    	printf ("\nIl triangolo è equilatero.\n");
    	return 0;
    }
    //Triangolo isoscele
    if (l1 == l2 || l1 == l3 ||l2 == l3) {
    	printf ("\nIl triangolo è iscoscele.\n");
    	return 0;
    }
    	
    //Triangolo rettangolo	
    if ((l1*l1) + (l2*l2) == l3*l3 || (l2*l2) + (l3*l3) == l1*l1 || (l1*l1) * (l3*l3) == l2*l2)
        printf ("\nIl triangolo è rettangolo.\n");
    	
    else printf ("\nIl triangolo è scaleno.\n");

	return 0;	
}
