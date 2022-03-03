#PRIMO CODICE (if,else(altrimenti/invece),elif(altrimenti))
--eta = int(input('Quanti anni hai?'))
  if eta > 30:
      print('Sei vecchio') #Bisogna lasciare lo spazio per includere nella funzione, sennò non farà parte
  
  elif eta == 30:          #Una volta = si usa per dichiarare una variabile, si usano 2 == per fare una comparazione
    print('Stai in pari')
 
  elif eta == 20:
    print('Hai 20 anni')
  
  else:
    print('Sei un giovincello')
____________________________________________________________
>= #maggiore uguale  
<= #minore uguale
!= #è diverso
== #uguale
> #maggiore
< #minore
________________________________________________________________
esempio
--password = input('Scrivimi la password')
  if != '123 stella':
    print('non conosci la password')
  else:
    print('Bravo conosci la password')
____________________________________________________________________
#SECONDO COICE
if TRUE: #Se è vero
 print('Ciao')
________________________________________________________________________
if 2 == 2.0:
  print('Uguali')
__________________________________________________________________________
eta = 30
quartiere = 'vomero'
if eta > 30 and quartiere == 'vomero':
  print('Ciao')
______________________________________________________________________________
ESPRESSIONI LOGICHE
and #Se entrambe sono vere fai questo
or #Se una sola è vera fai questo
not # Se sono false fail l'opposto
_________________________________________________________________________________
eta = 31
quartiere = 'vomero'
città = 'roma'
if eta > 30 and quartiere == 'vomero' or città == 'Napoli':  #le prime 2 vero, la 3 falso, quindi vero x falso = vero
  print('Ciao')
_______________________________________________________________________________________
vite = 31
bonus_vite = 1
livello = 8
if vite < 31 and livello == 8: #Se hai meno di 31 vite e stai all 8 livello print questo
  print ('game Over')
if vite < 31 and (livello == 8 or bonus_vita > 0): #Mettiamo le parentesi per far fare prima quella operazione, sarà falso x falso
  print('Hai una vita in più')
_____________________________________________________________________________________________
risposta_a = input('Ti piace viaggiare? y/n: ')
if risposta_a == 'y':
  risposta_b == input('Ti piace il Burundi? y/n: ')
  if risposta_b == 'y':
    print('Complimenti hai vinto')
  else:
    print('Mi spiace hai perso') #Se dici si 1 e si 2 hai vinto
else: 
  print('Peccato')
___________________________________________________________________________________________________________
#TERZO CODICE (for(esegui quest'operazione finchè non finisce il contatore), while(esegui quest'operazione finchè non è vera))
#Possono fare le stesse cose solo che il for continua fino alla fine rispetto a while
contatore = 1
while contatore < 11:
  print('contatore')
  contatore += 1
print ('Finito')
________________________________________________________________________________________________________________
print('''
====================
=INDOVINA IL NUMERO=
====================
''')
numero_segreto = 14
numero_inserito = int (input('indovina il numero segreto')
sbagli = 0
while numero_inserito != numero_segreto:
  print('Sbagliato')
  sbagli += 1 #Gli sbagli sono aumentano di 1 finchè non rispetti la condizione(numero_segreto)
  numero_inserito = int(input('Riprova dai'))
  print('Perfetto!Hai indovinato')
  print('Hai sbagliato solo:')
  print(sbagli)
________________________________________________________________________________________________________________
contatore = 1
while contatore < 11:
  print('contatore')
  contatore += 1
print ('Finito')

for contatore in range (1,11): #al posto di contatore potevamo scrivere x o c, è solo una vaiabile non conta nulla
   print(contatore)
 print('Finito')
_______________________________________________________________________________________
 for x in 'Ciao'
  print('Ciao') #Me lo andrà a scrivere una sotto all'altro
 /////////////////////////////////////////                      
RANGE #Prende tutti i numeri tra 2 numeri, se gli do 1 numero parte da 0, se scrviamo range(1,10,2) il terzo numero significa conta ogni 2, quindi ogni quanto deve contare
#Se la condizione è sempre vera continuerà all'infinito finchè non gli diciamo di fermarsi.
____________________________________________________________________________________
 whilw True:
  nome = input('inserisci il tuo nome o ESCI per uscire:')
  if (nome == 'ESCI') #break mi interrompe la funzione sopra che è in questo caso while
      break 
  print('Ciao',nome)
____________________________________________________________________________________
 for i in range(1,21)
  if i % 5 == 0: #Se i è divisibile per 5 e mi da come risultato 0, scrivilo
    continue #Riparte il ciclo for
  print (i)   
____________________________________________________________________________________
for i in range (11)
  pass #non serve a niente serve per non lasciare una funzione vuota
_____________________________________________________________________________________
for a in range (1,6):  
  for b in range (1,6):
   print(a, 'moltiplicato per', b, '=', a*b 
#Prima completa il range di sotto poi quello di sopra
_____________________________________________________________________________________________
while i < 5:
    print(i)
    i += 1 
else:
    print('numero:',i)
