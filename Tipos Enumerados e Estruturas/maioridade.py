# Análise:
#
# Determinar se uma pessoa é maior de idade ou não,
# retornando um tipo enumerado.
#
# Tipos de dados:
#
# Idade dada em anos como número inteiro


from enum import Enum, auto

class Idade(Enum):
    MAIOR_IDADE = auto()
    MENOR_IDADE = auto()

def maior_ou_menor_idade(idade: int) -> Idade:
    '''
    Define se uma pessoa é maior ou menor de idade com base na sua 'idade'

    Exemplos:

    >>> maior_ou_menor_idade(12).name
    'MENOR_IDADE'

    >>> maior_ou_menor_idade(32).name
    'MAIOR_IDADE'
    '''

    maioridade:Idade = Idade.MENOR_IDADE

    if idade >= 18:
        maioridade = Idade.MAIOR_IDADE

    return maioridade
