#Primo codice {funzione print}
print (' Ciao Mondo!') # per convenzione usiamo questo '

#Secondo codice {funzione print con testo}
print('io\'sono Antonio') #(lo conta come testo se mettiamo \)

#Terzo codice {per creare nuova riga}
print('ciao')
print('')
print('Antonio')
print ('Ciao\nAntonio') #se mettiamo \n fa nuaova riga
print ('ciao' + 'ciao') #li somma e li scrive insieme
print ('ciao' , 'ciao') #aggiunge uno spazio

#Quarto codie {ESERCIZIO}
print ('trent\'anni fa è nato il Python\nMa è sempre un gran bel linguaggio')

#Quinto codice {variabili}
topolino = 'un topo troppo cresciuto' #niente numeri iniziali nelle variabili
paperino = 'quando parla non si capisce'
pippo = 'idolo di tutti i bambini'
print (topolino) #per le variabili non dobbiamo mettere l'apicetto

#Sesto codice {variabili numerate}
paperino = 4 #sto dicendo che questo è un unmero intero, quindi ci darà come risultato un numero intero
pipp = 4.5 #numero con la virgola
minnie = 4. #per lui è sempre un numero con la virgola

#Settimo codice {valori true e false}
sono_un_somaro = True #hanno sempre la lettera maiuscola vero e falso
sono_un_somaro = False
paperina = 3_45_675_345_675_346_435_467_845_645_676_879_085 #_ è UN MODO PER SCRIVERE BENE UN NUMERO SENZA CHE PYTHON LO VA A VEDERE
print (0.000000000001) # lo converte direttamente in notazione scientifica esce (1e-20)

#Ottavo codice {varie funzioni matematiche}
print (0b11) #0 fa la conversione, se aggingiamo b, bianrio, o ottario, x essagesimale
2*2 #moltiplicazione
2/2#divisione
2-2#sottrazione
2+2#addizione
2//2#ci da un numero intero
5%2 #fa 5 diviso 2 e verra un numero con il resto, la perc ci fa uscire il resto 
2**5 #potenza

#Nono codice {applicazione variabili con funz. matematiche}
eta = 28 #senza le virgole è un numero, con è un testo #primo esempio
print (eta)

eta_più_grande = eta + 1    # secondo esempio 
print (eta_più_grande) #uscira 29

eta2 = eta*2  #terzo esempio
print (eta2)

eta += 1 #prendi la variabile eta e aggiungi 1   {comandi rapidi}
eta += 5 #prendi la variabile eta e moltiplicalo per 5, e cosi via per tutte le operazioni

print (eta + eta) #uscirà la somma

casa = '1'
print (casa + casa) #uscirà 11 poichè lo considera come testo e non come numero

print(eta*5)

#Decimo codice {esempio più funzione input}
print ('Antonio ha' , eta #prendi la variiabile eta , 'anni') #è tutto testo tranne eta

casa = 1.
casa *= 5 
print (casa) ci uscirà un numero con la virgola

input() #inserire qualcosa

nome = input ()
print ('Ciao' , nome)
