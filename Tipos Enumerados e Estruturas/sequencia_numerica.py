# Análise:
#
# Determinar dada uma ordem de 3 números qual o menor, qual o maior
# e qual está entre eles.
#
# Tipos de dados: números reais.


def sequencia_numerica(n1:float, n2:float, n3:float):

    '''
    Determina na ordem de 'n1', 'n2' e 'n3' qual o menor, qual o maior
    e qual está entre eles.

    Exemplos:

    >>> sequencia_numerica(1,2,3)
    Maior: 3 Meio: 2 Menor: 1

    >>> sequencia_numerica(10,3,7)
    Maior: 10 Meio: 7 Menor: 3

    >>> sequencia_numerica(1.2,1.6,1.153)
    Maior: 1.6 Meio: 1.2 Menor: 1.153
    
    '''
    maior = maior_3_numeros(n1,n2,n3)
    
    if n1 == maior:
        if n2 > n3:
            meio = n2
            menor = n3
        else:
            meio = n3
            menor = n2

    if n2 == maior:
        if n1 > n3:
            meio = n1
            menor = n3
        else:
            meio = n3
            menor = n1

    if n3 == maior:
        if n1 > n2:
            meio = n1
            menor = n2
        else:
            meio = n2
            menor = n1

    print("Maior: "+str(maior)+" Meio: "+str(meio)+" Menor: "+str(menor))

def maior_numero(n1:float,n2:float) -> float:
    '''
    Retorna qual número é maior: n1 ou n2
    '''

    maior = n1

    if n2 > maior:
        maior = n2


    return maior

def maior_3_numeros(n1:float,n2:float,n3:float) -> float:
    '''
    Retorna qual número é maior: n1, n2 ou n3
    '''
    return maior_numero(maior_numero(n1,n2),n3)
