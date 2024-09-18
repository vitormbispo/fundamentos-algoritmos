# Análise
# 
# Calcular o peso ideal de uma pessoa de acordo com seu gênero e altura
# usando a fórmula:
# P/ Homens: (72.7 * altura) - 58
# P/ Mulheres: (62.1 * altura) - 58
#
# Tipos de dados:
#
# Recebe a altura em metros e retorna o peso ideal em kilogramas.

def peso_ideal(altura:float, genero:str) -> float:
    
    '''
    Calcula o peso ideal dadas 'altura' e 'genero'.

    Exemplos:

    >>> peso_ideal(1.67,'M')
    63.41

    >>> peso_ideal(1.43,'F')
    44.1
    '''
    peso:float = 0.0

    if genero == 'M':
        peso = (72.7 * altura) - 58

    if genero == 'F':
        peso = (62.1 * altura) - 44.7

    return round(peso,2)
        
