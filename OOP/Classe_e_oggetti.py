class casa:
        def __init__(self,città, proprietario, piano, grandezza, stanze, prezzo):

        # Attributi di Istanza
                self.città = città
                self.propetario = proprietario
                self.piano = piano
                self.grandezza = grandezza
                self.stanze = stanze

                self.prezzo = prezzo
        
        

    #Metodo di tipo Get
        def scheda(self):
                return f'\nScheda "{self.città}"\n Propetario: {self.propetario}\n Piano: {self.piano}\n Grandezza: {self.grandezza}\n Stanze: {self.stanze}\n Prezzo: {self.prezzo}' 
    
giovanni = casa("Roma","giovanni","3",100, 6, "550.000")

marco = casa("Napoli","marco","5",200, 9, "700.000")

print("Il tipo di variabile costruita è:")
print(giovanni)
print(marco)

print("\nLa singola scheda è:")
print (giovanni.scheda())
print (marco.scheda())
print("\n\naltro metodo per visualizzare le informazioni (__dict__):")
print(giovanni.__dict__)
print(marco.__dict__)
