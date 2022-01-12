# classe calcolo combinatorio
import math
math.fattoriale(1000)
class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
        
        self.__stringa = str 
        
        return self.__stringa


    def charRipetuti(self):
        '''
        questo metodo deve creare un dictionary all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        
        esempi di dictionary sono presenti nel file elementi_base/dictionary.py
        '''
    def cerca(self):
        str= self.__stringa = stringa  
        it = 'words.italian.txt'

        f = open(it, 'r')
        line = f.readline()

        for line in f:  
            if str == line[:-1]:  
                print("vero")
    def confUtil(self):
        pass

    def fattoriale(n):
          if n < 2:
          return 1
      else:
          return n * fattoriale(n-1)
        '''
        implementare una qualunque versione della funzione fattoriale
        '''

    def coeffBinom(n, k):
          P = fattoriale(n)/fattoriale(K) * fattoriale(n-fattoriale(K))
        pass

    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        
        calcComb.fattoriale(self.n)
        return fattoriale(n)

    def nPermutConRip(self):
        
        calcComb.fattoriale(self.n)
        return fattoriale(n) / fattoriale(h) * fattoriale(k) * fattoriale(s)

    def permutSenzaRip(self):
        '''
        generare e restituire la lista di permutazioni SENZA ripetizione
        '''
        return 0

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
        
        calcComb.fattoriale(self.n)
        return P = fattoriale(n) / fattoriale(n-k)
      # non sa cosa sia il punto esclaamtivo. Devi dichiarare una funzione fattoriale
        # che prende in input n e restituisce il suo fattoriale.
        # se vai più sopra ho scritto anche la dichiarazione, devi implementarla. 
  
    def nDispSemplConRip(self):
        
        return n**k

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self):
        
        calcComb.fattoriale(self.n)
        return fattoriale(n) / fattoriale(k) * fattoriale(n-k)

    def nCombSemplConRip(self):
        
        calcComb.fattoriale(self.n)
        return fattoriale(n + k - 1) / fattoriale(k) * fattoriale(n-1)

    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0


    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0
    


