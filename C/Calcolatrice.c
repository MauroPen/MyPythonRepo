#include <stdio.h>

int main () {
	
	enum {somma, diff, moltiplicazione, divisione, potenza, finalizzatore};
	float num1, num2;
	float pot = 1.0;       									      //Serve per calcolo potenza
	int scelta;
	int i;                                                        //Iteratore
	
	
	printf ("Calcolatrice\n\nInserire un numero per iniziare.\n");
    scanf ("%f", &num1);
	
	do {printf ("\n%f\n", num1);
		printf ("\n(0) per somma\n(1) per differenza\n(2) per moltiplicazione\n(3) per divisione\n(4) per elevamento a potenza\n\n(5) per terminare\n\n");
	    scanf ("%d", &scelta);
	    
	    switch (scelta) {
		    
			case somma: {
			     printf ("\nInserisci un numero.\n");
				 scanf ("%f", &num2);
				 num1 += num2;
				 break;
			}
			case diff: {
				 printf ("\nInserisci un numero.\n");
				 scanf ("%f", &num2);
				 num1 -= num2;
				 break;
		    }
			case moltiplicazione: {
				 
				 num1 *= num2;
				break;
		    }
			
			case divisione: {
				 printf ("\nInserisci un numero.\n");
				 scanf ("%f", &num2);
				 if (num2 == 0 ) {
				 	printf ("\nErrore! Operazione impossibile\n");
				 	return 1;
				 }
				 else 
				 	num1 /= num2;
				break;
		    }
		    
		    case potenza : {                               
		    	 printf ("\nInserisci un numero intero.\n");
				 scanf ("%f", &num2);
				 
				 if (num1 == 0 && num2 ==0) {
		    		printf ("\n Errore! Operazione impossibile!\n");
		    		return 1;
		    	}
		    		
				 if (num1 == 0) {
				 	num1 = 0;
				 	break;
				 }
				 
				 if (num2 == 0) {
		    	    num1 = 1;
		    	    break;
		    	}	
		    	
		         while (num2 < 0) {
		         	printf ("\nInserisci un intero positivo.\n");
		         	scanf ("%f", &num2);		 	
				 }
				 pot = 1.0;
				 for (i = 1; i <= num2; i++)
				 	pot *= num1;
				
				num1 = pot;
				break;
			}
		    
		    case finalizzatore: {
		    	
				int risInt = num1;
				if (risInt == num1) {
				printf ("\nIl risultato è %d", risInt);       
				break;
		        }
		        else {
				printf ("\nIl risultato è %f", num1);
				break;
			}
		    }
		}
		
	} while (scelta != finalizzatore);
	
	return 0;		
	}
	
