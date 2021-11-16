class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self,str ):
         self.__stringa = str 
        
        return self.__stringa

    def charRipetuti(self):
        ogni chiave deve essere ogni carattere della stringa e edeve associare il valore alla chiave quante volte si ripete quel carattere
      stringa = {
        questo metodo deve creare un dictionary all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        
        esempi di dictionary sono presenti nel file elementi_base/dictionary.py
        '''

    def confUtil(self):
          str= "pop"  # nel caso di ruzzle, str deve contenere l'attributo di istanza
        it = 'words.italian.txt' # è possibile aggiungere tante variabili quanti file di lingua si posseggono

        f = open(it, 'r')
        line = f.readline()

        for line in f:  # per ogni riga del file vengono eseguite le righe di codice che seguono
        #    print(str) 
            if str == line[:-1]:  #bisogna eliminare l'ultimo carattere dalla parola contenuta nella riga del file
                print("vero")
        '''
        verificare se la STRINGA attributo di istanza è presente
        nel file word.italian.txt 
        '''
        pass

    def fattoriale(n):
        '''
        implementare una qualunque versione della funzione fattoriale
        '''

    def coeffBinom(n, k):
        P = n!/K!(n-K!)!
        

    # PERMUTAZIONI

    def nPermutSenzaRip(self):
      
        return P = n1 
     
      
    def nPermutConRip(self):
       
        return n!/a1! x a2! x ak!...

    
    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
      
        return P = n!/ (n-K)!

    def nDispSemplConRip(self):
       
        return P = n^k

    # COMBINAZIONI

    def nCombSemplSenzaRip(self):
        
        return P = n!/K!(n-k)!

    def nCombSemplConRip(self):
       
        return P = (n + k - 1)/K!(n-1)!

    


