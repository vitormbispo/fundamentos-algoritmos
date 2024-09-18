# Análise
#
# Recebe-se três valores a, b e c e se verifica se eles podem formar ou não um
# triangulo
#
# Tipos de dados:
#
# 'a', 'b' e 'c' são as medidas dos lados do triângulo todos em uma
# mesma unidade de medida qualquer dadas como números reais.
# Retorna uma verdadeiro quando se forma um
# triangulo, e falso quando não se forma.
#

def forma_triangulo(a:float, b:float, c:float) -> bool:
    '''
    Exemplo

    >>> forma_triangulo(2, 3, 1)
    True

    >>> forma_triangulo(5, 7, 1)
    False

    >>> forma_triangulo(10.7, 8.9, 3.4)
    True
    '''

    lado_maior:float = a 
    soma_menores:float = 0.0
    forma:bool = True

    if b > lado_maior:  
        soma_menores = lado_maior
        lado_maior = b
    else: 
        soma_menores = b 


    if c > lado_maior:
        soma_menores = soma_menores + lado_maior
        lado_maior = c
    else: 
        soma_menores = soma_menores + c

    if lado_maior > soma_menores:
        forma = False

    return forma
    
