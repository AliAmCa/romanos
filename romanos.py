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


def arabigo_a_romano(n):
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

def romano_a_arabigo(n):
    total =0
    for char in n:
        total += valores_romanos.key(char)
        print(total)
        print(valores_romanos.key(char))




