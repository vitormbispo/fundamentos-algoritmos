# Análise:
#
# Verificar se um número inteiro é par ou impar. A resposta deve ser dada po
# um tipo enumerado.
#
# Tipos de dados: recebe um número inteiro e retorna um tipo enumerado.

from enum import Enum, auto

class ParEImpar(Enum):
    PAR = auto()
    IMPAR = auto()


def par_ou_impar(n:int)->ParEImpar:
    '''
    Define se 'n' é PAR ou IMPAR.

    Exemplos:

    >>> par_ou_impar(2).name
    'PAR'

    >>> par_ou_impar(11).name
    'IMPAR'
    '''

    paridade: ParEImpar = ParEImpar.IMPAR

    if n % 2 == 0:
        paridade = ParEImpar.PAR

    return paridade
