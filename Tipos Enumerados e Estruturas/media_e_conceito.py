# Análise:
#
# Construir uma função que receba as notas e respectivos pesos
# do aluno e mostre a média ponderada e o conceito atribuido como na tabela
# abaixo:
#
#  Média      | Conceito
# [8,0;10,0]    A
# [7,0;8,0]     B
# [5,0;7,0]     C
# [0,0;5,0]     D
#
# Tipos de dados:
# Ambas notas e pesos são números reais (float) e o
# conceito é dado como um caracter (string)

def media_e_conceito(n1:float, n2:float, n3:float, p1:float, p2:float, p3:float) -> float:
    '''
    Calcula a média ponderada e conceito do aluno a partir de 3 provas

    Exemplos:

    >>> media_e_conceito(6.0, 8.0, 7.0, 2, 3, 4)
    B
    7.11

    >>> media_e_conceito(3.5, 4.3, 8.7, 1, 2, 5)
    C
    6.95

    >>> media_e_conceito(10.0, 10.0, 10.0, 5, 3, 7)
    A
    10.0

    >>> media_e_conceito(3.2, 4.6, 2.3, 2, 3, 1)
    D
    3.75
    
    '''

    media:float = round(((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3), 2)
    conceito:str = ''

    if 0.0 <= media < 5.0:
        conceito = 'D'
        
    if 5.0 <= media < 7.0:
         conceito = 'C'

    if 7.0 <= media < 8.0:
        conceito = 'B'

    if 8.0 <= media <= 10.0:
        conceito = 'A'

    print(conceito)
    return(media)
    

    
