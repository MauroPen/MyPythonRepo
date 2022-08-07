#include <stdio.h>

int main () {
	char parola [6], ban [6] = "wyjkx";
	int i,j;
	
	printf ("Verifica parola.\n\nInserire la parola (5 lettere) da verificare.\n");
	scanf ("%s", parola);
	
	for (i = 0; i <= 4; i++) {                 //Controllo lettere alfabeto italiano
		for (j = 0; j <= 4; j++)
			if (parola [i] == ban [j]) {
				printf ("\nLa parola inserita contiene almeno una lettera straniera.");
				return 1;
			}		
	}
	printf ("\nLa parola contiene solo lettere appartenenti all'alfabeto italiano.");
	
	for (i = 0; i <= 3; i++) {                 //Controllo ordine alfabetico
		if (parola [i] > parola [i+1]) {
		printf ("\n\nLe lettere non sono in ordine alfabetico.");
		return 1;	
	}
}
	printf ("\n\nLe lettere che compongono la parola sono anche in ordine alfabetico.");
	return 0;
}
