# Análise:
#
# Determinar se um ponto (x,y) em um plano está na origem, nos eixos ou em um quadrante.
# 
# Tipos de dados: pontos do plano como números inteiros

from enum import Enum, auto

class Pontos(Enum):
    ORIGEM = auto()
    EIXO_X = auto()
    EIXO_Y = auto()
    QUAD_1 = auto()
    QUAD_2 = auto()
    QUAD_3 = auto()
    QUAD_4 = auto()

def ponto_no_plano(x: int, y: int) -> Pontos:
    '''
    Determina se o ponto em 'x' e 'y' está na origem, eixos ou quadrantes

    Exemplos:

    >>> ponto_no_plano(0,0).name
    'ORIGEM'

    >>> ponto_no_plano(6,0).name
    'EIXO_X'

    >>> ponto_no_plano(0,6).name
    'EIXO_Y'

    >>> ponto_no_plano(3,4).name
    'QUAD_1'

    >>> ponto_no_plano(-5,6).name
    'QUAD_2'

    >>> ponto_no_plano(-3,-7).name
    'QUAD_3'

    >>> ponto_no_plano(3,-5).name
    'QUAD_4'
    '''

    pon: Pontos
    
    if x == 0 and y == 0:
        pon = Pontos.ORIGEM

    elif not(x != 0 and y != 0):
        if x == 0 and y != 0:
            pon = Pontos.EIXO_Y

        else:
            pon = Pontos.EIXO_X

    else:
        if x > 0 and y > 0:
            pon = Pontos.QUAD_1

        elif x < 0 and y > 0:
            pon = Pontos.QUAD_2

        elif x < 0 and y < 0:
            pon = Pontos.QUAD_3

        else:
            pon = Pontos.QUAD_4

    return pon
