#include <stdio.h>

int main () {
	int a, x;
	float ris=1.0;
	
	
	printf ("Calcolo di potenze ad esponente intero\n\nInserire la base\n");
	scanf ("%d", &a);
	printf ("Inserire l'esponente\n");
	scanf ("%d", &x);
	
	
	if (x==0) {                               //Caso esponente = 0
		printf ("Il risultato � 1");
		return 0;
	}
 	
 	
	
    if (a==0) {                               //Caso base = 0  
    	printf ("Il risultato � 0");
    	return 0;
	}
	
   
    if (x>0) {                                //Caso esponente > 0
	   do {
	ris = (ris * a);
	x=x-1;
    } while (x>0);
    
    printf ("Il risultato � %.0f", ris);
    return 0;
    }
    
   
    else {                                    // Caso esponente < 0
    do {
    ris = (ris * a);
    x=x+1;
    } while (x<0);
    
    printf ("Risultato in decimale (1) o in frazione(0)?\n\n");     //Frazione o decimale
    scanf ("%d", &a);
      if (a==0) {
	  
	     printf ("Il risultato � 1\\%.0f", ris);
         return 0;
	   }
	  else {
		printf ("Il risultato � %f", 1/ris);             
		return 0;
	  }
   }
}


