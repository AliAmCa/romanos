
from romanos import arabigo_a_romano, romano_a_arabigo, RomanError

class RomanNumber(object):
    def __init__(self, entrada):
        if isinstance(entrada, str):
            self.arabigo = romano_a_arabigo(entrada)
            self.romano = entrada
        
        elif isinstance(entrada,int):
            self.romano = arabigo_a_romano(entrada)
            self.arabigo = entrada

        else:
            raise TypeError("Tipo introducido incorrecto")
       
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.romano

    def __int__(self):
        return self.arabigo

    #Funcion mayor que
    def __gt__(self,valor):
        if not isinstance(valor, RomanNumber):
            raise TypeError("Tiene que ser un numero romano")
        return self.arabigo > valor.arabigo
        
            
        
    #Funcion menor que
    def __lt__(self,RN):
        if isinstance(RN, RomanNumber):
            return self.arabigo < RN.arabigo
        elif isinstance(RN, int or float):
            return self.arabigo < RN

    #Otras funciones de comparacion
    # x<=y
    def __le__(self,RN):
        if not isinstance(RN, RomanNumber):
            raise TypeError("Tiene que ser un numero romano")
        return self.arabigo <= RN.arabigo

    # x==y
    def __eq__(self,RN):
        if not isinstance(RN, RomanNumber):
            raise TypeError("Tiene que ser un numero romano")
        return self.arabigo == RN.arabigo
    
    # x!=y
    def __ne__(self,RN):
        if not isinstance(RN, RomanNumber):
            raise TypeError("Tiene que ser un numero romano")
        return self.arabigo != RN.arabigo

    # x>=y
    def __ge__(self,RN):
        if not isinstance(RN, RomanNumber):
            raise TypeError("Tiene que ser un numero romano")
        return self.arabigo >= RN.arabigo

    #Funcion suma
    def __add__(self, RN):
        if isinstance(RN, RomanNumber):
            return RomanNumber(self.arabigo + RN.arabigo)
        elif isinstance(RN, int ):
            return self.arabigo + RN
        else:
            raise TypeError("Tiene que ser un numero ")
   
    def __radd__(self,other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.arabigo + other.arabigo)
        elif isinstance(other, int):
            return self.arabigo + other
        else:
            raise TypeError("Tiene que ser un numero ")
       

    #Funcion resta
    def __sub__(self, RN):
        if isinstance(RN, RomanNumber):
            return RomanNumber(self.arabigo - RN.arabigo)
        elif isinstance(RN, int):
            return self.arabigo - RN
        else:
            raise TypeError("Tiene que ser un numero")
    
    def __rsub__(self, RN):
        if isinstance(RN, RomanNumber):
            return RomanNumber(RN.arabigo - self.arabigo)
        elif isinstance(RN, int):
            return RN - self.arabigo 
        else:
            raise TypeError("Tiene que ser un numero")


    #Funcion multiplicacion
    def __mul__(self,RN):
        if isinstance(RN, RomanNumber):
            return RomanNumber(RN.arabigo * self.arabigo)
        elif isinstance(RN, int):
            return RN * self.arabigo 
        else:
            raise TypeError("Tiene que ser un numero")

    def __rmul__(self,other):
        if isinstance(other, RomanNumber):
            return RomanNumber(other * self.arabigo)
        elif isinstance(other, int):
            return other * self.arabigo
        else:
            raise TypeError("Tiene que ser un número")

    #Funcion division
    def __truediv__(self,RN):
        if isinstance(RN, RomanNumber):
            return RomanNumber(self.arabigo//RN.arabigo)
        elif isinstance(RN, int):
            return self.arabigo//RN
        else:
            raise TypeError("Tiene que ser un numero ")

    def __rtruediv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(other.arabigo//self.arabigo)
        elif isinstance(other, int):
            return other//self.arabigo
        else:
            raise TypeError("Tiene que ser un numero")
        

    