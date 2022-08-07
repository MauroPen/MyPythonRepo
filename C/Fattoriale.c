#include <stdio.h>
int main () {
	long int contatore, fatt;
	printf ("Calcolo del fattoriale di un numero\n\nInserire un numero\n");
	scanf ("%d", &fatt);
	if (fatt==0 || fatt==1) {                                    //Terminazione precoce
		printf ("Fattoriale � uguale a 1\n");
		return 0;
	};
while (fatt < 0) {                                               //Condizioni di esistenza del valore
	printf ("Inserire un valore valido\n");
	scanf ("%d", &fatt);	
};
contatore = fatt;
while (contatore > 1) {                                          //Possibile eliminare contatore?
	contatore = contatore - 1;
	fatt = fatt * contatore;
};
printf ("Il fattoriale � %d\n", fatt);
return 0;
}
