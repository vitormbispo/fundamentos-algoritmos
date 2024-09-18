# Análise
#
# Projetar uma função que recebe 3 número obrigatoriamente em ordem crescente
# e mais um número fora dessa regra. Retornar a posição do número fora da regra.
#
# Tipos de dados:
#
# Todos os números devem ser reais.

def posicao_numero(n1:float, n2:float, n3:float, x:float) -> int:
    '''
    Retorna a posição do número X na ordem crescente entre os números
    'n1', 'n2' e 'n3'.

    Exemplos:
    >>> posicao_numero(1, 2, 4, 3)
    2

    >>> posicao_numero(1, 2, 3, 5)
    3

    >>> posicao_numero(28, 40, 95, 32)
    1
    '''

    pos:int = 0
    
    if x <= n1:
        pos = 0

    if n1 < x <= n2:
        pos = 1

    if n2 < x <= n3:
        pos = 2

    if x > n3:
        pos = 3

    return pos
        
