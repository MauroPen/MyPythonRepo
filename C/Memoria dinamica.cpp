#include <stdio.h>
#include <stdlib.h>

typedef struct x {
	int num;
	struct x *next;
} elemento;

typedef elemento *pointer;

void add (pointer);
void printall (pointer);
void search (pointer, int);
void elimina (pointer, int);		


int main () {
	int scelta, inserim, ricerca, del;
	pointer p1 = NULL, temp;                    //Iniziale, non deve mai cambiare; pointer d'appoggio;
	

	
	printf ("Memoria dinamica\n\n");
	
	do {
		printf ("\nSeleziona cosa fare\n\n(1) per aggiungere elementi\n(2) per stampare tutti gli elementi salvati\n(3) per cercare un elemento\n(4) per eliminare un elemento\n\n");
		scanf ("%d", &scelta);
		
		switch (scelta) {
			
			case (1): {
				if (p1 == NULL) {
					printf ("\nInizializzare il primo elemento\n");
					scanf ("%d", &inserim);
	
					p1 = (pointer) malloc (sizeof (elemento));		
					p1->num = inserim;
					p1->next = NULL;	
				}
				add (p1);
				break;
			}
			
			case (2): {
				printall (p1);
				break;
			}
			
			case (3): {
				printf ("\nInserire il valore da ricercare all'interno della lista\n\n");
				scanf ("%d", &ricerca);
				search (p1, ricerca);
				break;
			}
			
			case (4): {
				printall (p1);
				printf ("\n\nScegliere che valore eliminare dalla lista\n");
				scanf ("%d", &del);
					if (p1->num == del) {
						temp = p1;
						p1 = p1->next;
						free (temp);
					}
					else	
						elimina (p1, del);						
			}
			
			default: break;
		}
		
	} while (scelta != 0);
	
return 0;
}

void add (pointer p1) {
	int ctrl = 0;
	int inserim = 1;
	
		while (ctrl == 0) {
			
			if (p1->next == NULL) ctrl = 1;
	 
			else p1 = p1->next;
		}
	
	while (inserim != 0) {
		
	printf("\nInserire il valore da salvare. (0) per terminare\n");
	scanf ("%d", &inserim);
	
		if (inserim == 0) break;
	
		else {
		
			p1->next = (elemento*) malloc (sizeof(elemento));
			p1->next->num = inserim;
			p1->next->next = NULL;
			p1 = p1->next;
		}
	}
}

void printall (pointer p1) {
	
	while (p1 != NULL) {
		printf ("\n%d\n", p1->num);
		p1 = p1->next;
	}
}

void search (pointer p1, int ricerca) {				//Ricorsione

	if (p1 == NULL)
		printf ("\nValore non presente all'interno della lista!\n");
		
	else 
		if (p1->num == ricerca)
			printf ("\nIl valore è stato trovato all'interno della lista\n");
			
		else {
			p1 = p1->next;
			search (p1, ricerca);
		}
	}

void elimina (pointer p1, int del) {				//Ricorsione
	pointer temp;
	
	if (p1->next == NULL) 
		printf ("\nErrore! Valore non trovato all'interno della lista. Riprovare\n");
	
	else		
		if (p1->next->num == del) {
			temp = p1->next;
			p1->next = temp->next;
			free (temp);
		}
		
		else {
			p1 = p1->next;
			elimina (p1, del);
		}
	
}




