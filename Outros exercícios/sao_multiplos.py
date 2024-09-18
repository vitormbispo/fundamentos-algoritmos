# Análise
#
# Determina se um número é múltiplo ou não
#
# Tipos de dados:
#
# Todos os números de entrada são números reais e a saída é Verdadeira ou Falsa.

def sao_multiplos(n1:float, n2:float) -> bool:
    '''
    Verifica se 'n1' e 'n2' são múltiplos

    Exemplos:

    >>> sao_multiplos(2, 78)
    True

    >>> sao_multiplos(108, 5)
    False

    >>> sao_multiplos(5679, 3)
    True
    
    '''
    maior = n1
    menor = n2
    multiplo = False

    if n2 > maior: 
        menor = maior 
        maior = n2 

    if maior % menor == 0:
        multiplo = True

    return multiplo
