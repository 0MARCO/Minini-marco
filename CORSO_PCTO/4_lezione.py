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
_______________________________________________
lista = [1,2,3]
nuova_lista = lista
lista[0] = -5 #prendi 1 e cambiamelo in -5
print(lista)
print(nuova_lista)
_________________________________________________
lista = [1,2,3]
nuova_lista = lista[:] #Deve essere uguale agli indici della prima, mi darà la nuova e la vecchia lista
lista[0] = -5 
print(lista)
print(nuova_lista)
__________________________________________________
numeri = []
for i in range(1,100):
  numeri.append(i)
print(numeri) #Ci darà tutti i numeri da 1 a 100
______________________________________
numeri = []
for i in range(1,100):
  numeri.append(i)
print(numeri) 

numeri = [i for i in range(1,101) if i % 3 != 0] #Ci andrà a stampare tutti i numeri divisibili per 3
print('numeri')
____________________________________________
numeri = [1,2,3]
paesi = ['IT','UK',FR']
celle = [['A1','A2','A3'], ['B1','B2','B3']]
print(celle[0][2]) #Se metto un solo 0 chiedo la prima lista, se metto un secono numero prendo l'elemento di quella lista       
_____________________________________________________
celle = [['A1','A2','A3'], ['B1','B2','B3']]
for x in cella:
     for y in x:
        print('elemento:',y)
__________________________________________________________
lista1 = ['Roma','Napoli']
lista2 = ['Milano','Bari']
lista_somma = lista1 + lista2
_____________________________________________________________
lista_numeri = [0,1] * 10 #scriverà 0 e 1 per 10 volte
print(lista_numeri)
______________________________________________________________
nome = 'Antonio'
 print(nome[4]) #Scriverà solo la n

nome = 'Antonio'
nome_maiuscolo = nome.upper() #Mette tutto in maiuscolo         
print(nome_maiuscolo)         
_________________________________________________________________________
lista = []
tuple = () #Tutte le operazioni non sono consentite rispetto alla lista, si può scrivere pure senza parentesi tonde  
print (len(tuple))
________________________________________________________________________
SECONDO CODICE #Dizionario, utilizza parentesi graffe
emails = {
  'Antonio' : gg
  'Marco' : mm
print(emails['Antonio']) # ci darà l'email di antonio  
__________________________________________________________________________
voti ={}
voti['Alessandro'] = '3'
voti['Marco'] = '8' 
print(voti['Alessandro'])  
voti.update({'Alessandro':'2'})
print(len(voti)) #Mi dirà quanti studenti ci staranno all'interno
