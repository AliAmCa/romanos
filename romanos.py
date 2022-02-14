valores_romanos = {
    1 : 'I',
    4 : 'IV',
    5 : 'V',
    9 : 'IX',
    10 : 'X',
    40: 'XL',
    50 : 'L',
    90 : 'XC',
    100 : 'C',
    400 : 'CD',
    500 : 'D',
    900 : 'CM',
    1000 : 'M'

}

valores_romanosT = [
    
    (1000 , 'M'),
    (900,'CM'),
    (500 ,'D'),
    (400,'CD'),
    (100 , 'C'),
    (90, 'XC'),
    (50 ,'L'),
    (40,'XL'),
    (10 ,'X'),
    (9,'IX'),
    (5,'V'),
    (4,'IV'),
    (1,'I')
]


class RomanError(Exception):
    pass

def valida_numero(n):
    if not isinstance(n,int):
        raise TypeError(f"{n} debe ser de tipo int")

    if n<=0:
        raise ValueError(f"{n} debe ser un entero positivo")

def arab_a_roman_mayor(n):
    romano =[]
    while not n<1000:
        resto = n%1000
        
        romano.append(arabigo_a_romano(resto))
        
        n = n//1000
    
    romano.append(arabigo_a_romano(n))
    numero =""
    cont=len(romano)-1
    numero =(len(romano)-1)*"("

    for r in reversed(romano):
        if cont==0:
            numero +=r
        else:
            numero +=r +")"
        cont-=1
    
    return numero
    




def arabigo_a_romano(n):
    valida_numero(n)
    romano = ""
    if n>3999:
        romano = arab_a_roman_mayor(n)
    else:
        resto = None
        while resto != 0:
            for valor,simbolo in valores_romanosT:
                if n >= valor:
                    break
            
            cociente = n // valor
            resto = n % valor
            romano += cociente * simbolo
            n = resto
    return romano

def validaSimbolo(simbolo):
                
    if simbolo not in '()IVXLDCM':
        raise RomanError(f"{simbolo} no es un numero romano")

def romano_a_arabigo(r):
    r = r.upper()
    total =0
    d = {}
    for clave, valor in valores_romanos.items():
        d[valor]= clave

    contador=1
    
    valor_anterior=0
    char_anterior= ""
    for char in r:
        validaSimbolo(char)
        
        valor_actual= d[char]
        
        #comprobar repeticiones
        if char == char_anterior:
            contador +=1
                               

            if char in 'VLD' and contador > 1 :
                raise RomanError(f"Demasiadas repeticiones de {char} ")
            elif contador > 3:
                raise RomanError(f"Demasiadas repeticiones de {char} ")
           


        else: 
            if contador >1 and valor_actual>valor_anterior:
                  raise RomanError(f"Las repeticiones de {char} no pueden restar")
            contador =1

        #Comprobar valores si suman o restan

        if valor_actual<= valor_anterior: #si el valor actual es menor que el anterior, lo sumamos al total
            total+=valor_actual
            valor_anterior = valor_actual
            

        else: # si el valor actual es mayor, resto al valor anterior al total, y le sumo valoractual menos valor anterior

            if char_anterior == 'V' or char_anterior == 'L' or char_anterior == 'D' :
                raise RomanError(f"{char_anterior} no puede restar")

            # Restas prohibidas
            if char_anterior =='I' and char not in 'VX' or char_anterior == 'X' and char not in 'LC' or char_anterior == 'C' and char not in 'DM' :
                raise RomanError(f"{char_anterior} no puede restar a {char} ")   
            

            
            total += valor_actual-2*valor_anterior
            valor_anterior = valor_actual

        char_anterior = char

    return total
        

def roman_a_arab_mayor(r):
   
    listaNumeros=[]
    cadena=""
    for char in r:
        
        if char not in '()':
            cadena+=char
        
        if char == ')':  
            listaNumeros.append(str(romano_a_arabigo(cadena)))
            cadena =""
        
    listaNumeros.append(str(romano_a_arabigo(cadena)))
    cadenaTotal=""
    for num in listaNumeros:
        cadenaTotal+= num
    
    return int(cadenaTotal)




