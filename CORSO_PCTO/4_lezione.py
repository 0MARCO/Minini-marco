PRIMO CODICE(Liste)
citta_1 = 'Napoli' #Variabili
città_2 = 'Roma'
lista_città = ['Napoli','Roma','Milano','Bari','Caserta'] #Lista
print(lista_città)
print(lista_città[0]) #Se mettiamo 0 ci darà la città Napoli, se mettiamo 1 Roma ecc... # Da destra verso sinistra
print(lista_città[-1]) #Fa la stessa cosa da sinistra verso destra
print(lista_città[0:2]) # Cosi gli andiamo a dare un range, il 2 non verrà contato e andrà da 0 a 1
print(lista_città[:2]) # Dalla seconda a scendere 
print(lista_città[2:]) #Parti da 2 fino alla fine
print(lista_città[:]) #Prendi tutti i valori della lista
______________________________________________________________________
lista_città = ['Napoli','Roma','Milano','Bari','Caserta']
del lista_città[1] #Possiamo dire quale elemento vogliamo eliminare, in questo caso leverà Roma
del lista_città[1:] #Elimina tutto quello che c'è da 1 in poi

#Quando metto i : sto usando gli indici, quindi è il contenuto
#Se non mettiamo niente dento andrà a cancellare la lista

lista_città.append('Salerno') #Per aggiungere alla lista un elemento però alla fine
lista_città.insert(1,'Salerno') #Per aggiungere alla lista un elemento in una determinata posizione, in questo caso 1
print(lista_città)
________________________________________________________________________
lista_città = ['Napoli','Roma','Milano','Bari','Caserta']
for x in lista_città:
  print('La città è:',x) #Lo farà per tutte le città
for città_indice in range(len(lista_città)): #Ci dirà quanti elementi ci sono in quella lista
  print('Indice:',città-indice,'Città:',for x in lista_città[citta_indice]) #Scriverà Indice 0 Città: Napoli e così via
___________________________________________________________________________
spese = [1,2,4,6]
somma = 0
for spesa in spese:
  somma += spesa
print('Hai speso:',somma) #Ci darà quanto abbiamo speso, quindi 13
____________________________________________________________________________
citta_1 = 'Roma' 
città_2 = 'Napoli'
temp = città_1
città_1 = città_2
città_2 = temp #Per scambiare di posto dobbiamo creare una terza variabile
____________________________________________________________________________
lista_città = ['Napoli','Roma','Milano','Bari','Caserta']
lista_città[0], lista_città[1] = lista_città[1], lista_città[0] #Scambierà di posto le liste #Napoli con Roma

lista_città.sort() #Per mettere in ordine alfabetico per sempre
print(lista_città)
lista_città.sort(reverse=True) #Metterà in ordinea l contrario
print(lista_città)

print(sorted(lista_città)) #Metterà sempre in ordine, non per sempre
_________________________________________________________________________
invitati = ['Antonio'.'Marco','Giulio','Alessandro']
nome = input('Come ti chiami?')
if nome in invitati:  #Legge tutto il codice anche se non è presente nella lista
  print('Benvenuto')

else:
  print('Nessuno ti ha invitato')
____________________________________________
if nome not in invitati:  #Se tu sbagli ad accedere non proseguo
  print('Accesso negato')

else:
  print('Benvenuti')
  password = input('Password')
