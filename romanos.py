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
'''
def valida_numero(n):
    if not isinstance(n,int):
        raise TypeError(f"{n} debe ser de tipo int")
    if n<=0:
        raise ValueError(f"{n} debe ser un entero positivo")

'''
def arabigo_a_romano(n):
    #valida_numero(n)
    romano = ""
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

def romano_a_arabigo(r):
    total =0
    d = {}
    for clave, valor in valores_romanos.items():
        d[valor]= clave

    valor_anterior=0
    for char in r:
        
        valor_actual= d[char]
        if valor_actual<= valor_anterior:
            total+=valor_actual
            valor_anterior = valor_actual

        else:
            total-= valor_anterior
            total += valor_actual-valor_anterior
            valor_anterior = valor_actual

    return total
        




