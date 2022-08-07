// Esempio programmazione: VISITA AL PUB
// by Florian Daniel
// 26 Ottobre 2016
//
// Funzionalità  supportate:
//   - ispezione menu birre
//   - incremento tempo
//   - calcolo tasso alcolemico
//   - calcolo conto
//
// Attenzione: il codice non valida in maniera esaustiva
//             la correttezza degli input dell'utente!

#include <stdio.h>
#include <string.h>


// dichiarazione dimensione degli array
#define LUNGH_MENU 5
#define MAX_BIRRE 5

// dichiarazione parametri per formula di Widmark
#define PESO_SPEC_SANGUE 1.055
#define FATTORE_WIDMARK_UOMO 0.73
#define FATTORE_WIDMARK_DONNA 0.66
#define CONVERSIONE_ABV_ABW 0.8

// dichiarazione costante di assorbimento alcol/minuto
#define ASSORBIMENTO_MINUTO 0.0025


// dichiarazione dei tipi dei dati gestiti dall'applicazione

typedef struct {
   char  nome[30];
   char  stile[30];
   char  colore[30];
   float ABV;
   int   volume;
   float prezzo;
} Birra;

typedef struct {
   char sesso;
   int  peso;
} Persona;

typedef struct {
   int birra_consumata;
   int ora;
} Consumo;

typedef Birra Menu[LUNGH_MENU];



int main() {
   
   // inserimento delle birre alla spina nell'array
   Menu AllaSpinaOggi;
   strcpy(AllaSpinaOggi[0].nome, "Gaina");
   strcpy(AllaSpinaOggi[0].stile, "India Pale Ale");
   strcpy(AllaSpinaOggi[0].colore, "ramato opalescente");
   AllaSpinaOggi[0].ABV = 6.0;
   AllaSpinaOggi[0].volume = 500;
   AllaSpinaOggi[0].prezzo = 6.0;
   strcpy(AllaSpinaOggi[1].nome, "Cevedale");
   strcpy(AllaSpinaOggi[1].stile, "American Pale Ale");
   strcpy(AllaSpinaOggi[1].colore, "giallo opalescente");
   AllaSpinaOggi[1].ABV = 5.2;
   AllaSpinaOggi[1].volume = 500;
   AllaSpinaOggi[1].prezzo = 5.5;
   strcpy(AllaSpinaOggi[2].nome, "Tipo Pils");
   strcpy(AllaSpinaOggi[2].stile, "Pils/Lager");
   strcpy(AllaSpinaOggi[2].colore, "giallo paglierino");
   AllaSpinaOggi[2].ABV = 4.5;
   AllaSpinaOggi[2].volume = 400;
   AllaSpinaOggi[2].prezzo = 4.2;
   strcpy(AllaSpinaOggi[3].nome, "Paulaner");
   strcpy(AllaSpinaOggi[3].stile, "Weissbier");
   strcpy(AllaSpinaOggi[3].colore, "giallo torbido");
   AllaSpinaOggi[3].ABV = 5.5;
   AllaSpinaOggi[3].volume = 500;
   AllaSpinaOggi[3].prezzo = 5.2;
   strcpy(AllaSpinaOggi[4].nome, "Duff");
   strcpy(AllaSpinaOggi[4].stile, "Simpson ale");
   strcpy(AllaSpinaOggi[4].colore, "giallo simpseriano");
   AllaSpinaOggi[4].ABV = 9.0;
   AllaSpinaOggi[4].volume = 330;
   AllaSpinaOggi[4].prezzo = 7.0;
   
   // variable che conterrà  la scelta dell'utente nel menù di primo livello
   enum {ordina, fai_passare_tempo, mostra_tasso, paga} SceltaAzione;
   
   // dichiarazione variabili relative all'utente
   Persona Cliente;
   int SceltaBirra;
   Consumo Bevuta[MAX_BIRRE];
   int birre_bevute = 0;
   int FaiQualcosa;
   
   // dichiarazione variabili conteggio tempo
   int ora;
   int ora_ultima_bevuta = 0;
   int i;
   
   // saluto e input sesso/peso del cliente
   printf("Benvenuto nel nostro pub!\n\nFornisci:\n\n");
   printf("  Sesso (m/f): ");
   scanf("%c", &Cliente.sesso);
   printf("  Peso: ");
   scanf("%d", &Cliente.peso);
   while ( getchar() != '\n' ) {
   printf("\nScusa, non ho capito. Inserisci un numero che indichi il Suo peso\n");
   scanf ("%d", &Cliente.peso); // svuota input buffer
}
   do { // ciclo di controllo principale: termina quando si paga
      
      // input scelta del cliente
      printf("\nCome ti posso essere utile?\n\n");
      printf("Opzioni:\n\n"
             "  0 = ordina una birra\n"
             "  1 = fai passare 10 minuti\n"
             "  2 = mostra tasso alcolemico\n"
             "  3 = paga ed esci\n\n");
      printf("Scelta: ");
      scanf("%d", &SceltaAzione);
      
      switch (SceltaAzione) { // gestione scelte del cliente
            
            // visualizza le birre alla spina e permette al cliente di sceglierne una
         case ordina: {
         	FaiQualcosa = -1;
            printf("\nEcco le birre che abbiamo alla spina:\n\n");
            for (i = 0; i < LUNGH_MENU; i++) {
               printf("  %d = %s, %s, %s, %2.2f alc, %d ml, %2.2f euro\n",
                      i, AllaSpinaOggi[i].nome, AllaSpinaOggi[i].stile,
                      AllaSpinaOggi[i].colore, AllaSpinaOggi[i].ABV,
                      AllaSpinaOggi[i].volume, AllaSpinaOggi[i].prezzo);
            }
            printf("\nScelta: ");
            scanf("%d", &SceltaBirra);
            printf ("\nOttimo, ecco la tua %s, buona bevuta!\n", AllaSpinaOggi[SceltaBirra].nome);
            
            // tracciamento della bevuta e incremento numero birre bevute
            Bevuta[birre_bevute].birra_consumata = SceltaBirra;
            Bevuta[birre_bevute].ora = ora;
            birre_bevute++;
            ora_ultima_bevuta = ora;
            
            while (FaiQualcosa < 0) {
            	printf("\n\nQuando vuoi fare altro, chiamami! (Digita qualsiasi numero)\n\n\n\n");
            	scanf("%d", &FaiQualcosa);
			}
            break;
         }
            
            // incremento fisso del tempo percorso
         case fai_passare_tempo: {
         	FaiQualcosa = -1;
            ora += 10;
            printf("\nL'ora attuale è: %d.\n", ora);
             while (FaiQualcosa < 0) {
            	printf("\n\nQuando vuoi fare altro, chiamami! (Digita qualsiasi numero)\n\n\n\n");
            	scanf("%d", &FaiQualcosa);
			}
            break;
         }
            
            // calcolo e stampo del tasso alcolemico
         case mostra_tasso: {
         	FaiQualcosa = -1;
            float tasso_alcolemico = 0;
            float fattore = (Cliente.sesso == 'm') ? FATTORE_WIDMARK_UOMO :FATTORE_WIDMARK_DONNA;
            
            // calcolo della quantita' di alcol ingerito
            for (i = 0; i < birre_bevute; i++) {
               tasso_alcolemico += AllaSpinaOggi[Bevuta[i].birra_consumata].volume *
               AllaSpinaOggi[Bevuta[i].birra_consumata].ABV/100 *
               CONVERSIONE_ABV_ABW * PESO_SPEC_SANGUE /
               Cliente.peso / fattore;
            }
            
            // decremento tasso alcolemico per smaltimento (se applicabile)
            if (ora - ora_ultima_bevuta > 30)
               tasso_alcolemico -= (ora - ora_ultima_bevuta - 30) * ASSORBIMENTO_MINUTO;
            
            // stampa tasso alcolemico
            printf("\nIl tuo tasso alcolemico attuale è %2.2f g/l.\n", tasso_alcolemico);
             while (FaiQualcosa < 0) {
            	printf("\n\nQuando vuoi fare altro, chiamami! (Digita qualsiasi numero)\n\n\n\n");
            	scanf("%d", &FaiQualcosa);
			}
            break;
         }
            
            // calcolo conto da saldare
         case paga: {
            float conto = 0.0;
            
            // stampa consumazioni individuali
            printf("\nHai consumato:\n\n");
            for (i = 0; i < birre_bevute; i++) {
               conto += AllaSpinaOggi[Bevuta[i].birra_consumata].prezzo;
               printf("  %s, %2.2f\n", AllaSpinaOggi[Bevuta[i].birra_consumata].nome, AllaSpinaOggi[Bevuta[i].birra_consumata].prezzo);
            }
            
            // stampa conto
            printf("\nIl conto totale è di %2.2f euro.\n\n", conto);
            break;
         }
            
            // gestione di input diversi da 0, 1, 2, 3
         default: {
            printf("\nScusa, non ho capito.\n");
            while ( getchar() != '\n' ); // svuota input buffer
         };
      }
   } while (SceltaAzione != paga); // termina dopo il pagamento
   
   return 0;
}






