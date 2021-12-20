#Primo codice (funzione input)
  input() #quello che gli andiamo a dare è sempre un valore testo e non puo assumere come valore di un numero, solo tramite questi comandi
  
  ciao = '58' 
  int(ciao) #trasforma il testo in un numero senza virgola
  float(ciao) #Per trasformare il testo in un numero con la virgola
  str(ciao) #Trasforma il numero in testo
  
---ESEMPIO 1
  altezza_cm = input('Converti cm in piedi: Quanto sei alto?')
  int(altezza_cm)
  print('la tua altezza in piedi è:',altezza_cm/30.48) #La virgola indica che c'è qualcos altro da fare, non andrà poichè altezza non è un numero con la virgola, quindi basta modificare
    print('la tua altezza in piedi è:',float(altezza_cm)/30.48)
    altezza_cm = float(input('Converti cm in piedi: Quanto sei alto?')) #anzicchè farlo nella funzione print possiamo trasformarlo anche all'inizio
  
---ESEMPIO 2
  temp_c = 33
  temp_f = float(temp_c) * 1.8 + 32
  temp_f #Ci da il risulato
  str (temp_f) # Ci da il risultato il testo
  print ('la tua temperatura è di',str(temp_c), 'gradi celsius')

#Secondo codice(operazioni matematiche)
  print (+12) # ci da come risultato 12, giustamente con il + non esce 
  print(-12) #Ci da come risultato -12

  3 ** 3 * 3 / 3 // 3 % 3 + 3 - 3 #Ordine di come python svolge le operazioni
  3 + 3 - ((3+3) * (3+3)) #Anzicchè usare le quadrate mettiamo più parentesi tonde

  2 ** 2 ** 3 #Python svolge le potenze da destra verso sinistra, quindi 3 elevato alla 2, poi il risultato elevato alla 2
  print (0.1) #ci da come risultato 0.1
  print (0.1 + 0.1 + 0.1) #Ci da come risultato 0.3000, poichè è un errore di python mentre fa un conversione, prima binario e poi in decimale

#Terzo codice(funzione len)
  len('ciao') #Ci dice la lunghezza di una determinata frase o stringa, se mettiamo gli spazzi egli conterà anche gli spazzi o anche i simboli
  lunghezza = len('ciao') #Possiamo metterlo ancher nella funzione
  lunghezza # Ci da la lunghezza di ciao

  #Quarto codice()

#Quinto codice()

#Sesto codice()

#Settimo codice()

#Ottavo codice()

#Nono codice()
