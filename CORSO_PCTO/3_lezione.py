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
///////////////////////////////////////////////
>= #maggiore uguale  
<= #minore uguale
!= #è diverso
== #uguale
> #maggiore
< #minore
///////////////////////////////////////////////
esempio
--password = input('Scrivimi la password')
  if != '123 stella':
    print('non conosci la password')
  else:
    print('Bravo conosci la password')
///////////////////////////////////////////////
#SECONDO COICE
if TRUE: #Se è vero
 print('Ciao')
///////////////////////////////////////////////
if 2 == 2.0:
  print('Uguali')
//////////////////////////////////////////////
eta = 30
quartiere = 'vomero'
if eta > 30 and quartiere == 'vomero':
  print('Ciao')
/////////////////////////////////////////////
ESPRESSIONI LOGICHE
and #Se entrambe sono vere fai questo
or #Se una sola è vera fai questo
not # Se sono false fail l'opposto
///////////////////////////////////////////
eta = 31
quartiere = 'vomero'
città = 'roma'
if eta > 30 and quartiere == 'vomero' or città == 'Napoli':  #le prime 2 vero, la 3 falso, quindi vero x falso = vero
  print('Ciao')
///////////////////////////////////////////
vite = 31
bonus_vite = 1
livello = 8
if vite < 31 and livello == 8: #Se hai meno di 31 vite e stai all 8 livello print questo
  print ('game Over')
if vite < 31 and (livello == 8 or bonus_vita > 0): #Mettiamo le parentesi per far fare prima quella operazione, sarà falso x falso
  print('Hai una vita in più')
