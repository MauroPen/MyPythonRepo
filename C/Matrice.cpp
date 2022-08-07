#include <stdio.h>

typedef int matrice [3][3];

int main () {
	int i, j;
	matrice a;
	
	printf ("Inserire i valori da inserire nella matrice\n");
	
	for (i=0; i<3; i++) {
		for (j=0; j<3;j++) 
		scanf ("%d", &a[i][j]);
	}
	
	for (i=0; i<3; i++) {
		for(j=0; j<3; j++)
		printf (" %d ", a[i][j]);
	printf ("\n");	
	}
	return 0;
}
