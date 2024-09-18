# Análise
#
# Determinar se dois números inteiros são múltiplos ou não.
# Retornar um tipo enumerado como resultado.
#
# Tipos de dados: números inteiros

from enum import Enum, auto

class Multiplo(Enum):
    NAO_MULTIPLOS = auto()
    MULTIPLOS = auto()

def sao_multiplos(n1:int, n2:int)-> Multiplo:
    '''
    Determina se 'n1' e 'n2' são múltiplos

    Exemplos:

    >>> sao_multiplos(2,4).name
    'MULTIPLOS'

    >>> sao_multiplos(103,5).name
    'NAO_MULTIPLOS'

    >>> sao_multiplos(429,3).name
    'MULTIPLOS'

    >>> sao_multiplos(256,256).name
    'MULTIPLOS'
    '''

    multi: Multiplo = Multiplo.NAO_MULTIPLOS

    if n1 % n2 == 0 or n2 % n1 == 0:
        multi = Multiplo.MULTIPLOS

    return multi
