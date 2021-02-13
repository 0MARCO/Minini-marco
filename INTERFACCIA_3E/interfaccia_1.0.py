#Il codice è stato realizzato da Minini,Bottone,Scalese,Botta
import string
import numpy as np
import matplotlib.pyplot as plt
from guizero import App, Text, Textbox

# usiamo il metodo readlines 
# per ottenere una lista di righe del file

# stampiamo la prima riga
# print(f.readline()) 

# possiamo fare un ciclo e prendere riga per riga 

coordX = []
coordY = []

# da notare che posso fare un ciclo all'interno di un file
# direttamente sulle righe

def apri file():

    f = open("dati.txt", 'r')   # apriamo il file in lettura
    for riga in f:
    valori = str(f.readline())  # converto in stringa la riga
    Nval = len(valori)          # conto il numero di caratteri
    valori = valori.strip('\n') # elimino i lterminatore di riga
    valori = valori.split(',')  # separo la stringa in due numeri
    valori = list(valori)       # converto in lista
    print(valori)
    coordX.append(int(valori[0])) # aggiungo la coordinata X
    coordY.append(int(valori[1])) # aggiungo la coordinata Y

    f.close()  # chiudiamo il file

    print ("X: ",coordX)
    print ("Y: ",coordY)

# ordiniamo le liste
    coordX.sort()
    coordY.sort()
  
    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

# stampo il tipo di dati delle coordinate
   print(type(coordX))
   print(type(coordY))

# ora sono pronte per essere usate anche nei grafici

   plt.title("grafico python prodotto intermedio")
   plt.scatter(coordX,coordY)
   plt.xlabel('X')
   plt.ylabel('Y')
   plt.show()



app = App(title='Interfaccia')

hello_text = Text(app, text='GRAFICO', font='Helvetica', size=20)

whatever = TextBox(app, width=50, multiline=True, height=2)
whatever.value='Dati'

push = PushButton(app, text='premi', command= apri file)
push.width=10
push.height=5





app.display()
