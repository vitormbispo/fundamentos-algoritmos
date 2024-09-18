# Análise:
#
# Projetar uma função que calcule o imposto que um cidadão deve pagar de acordo
# com sua renda, considerando que a unidade monetária é 'dinheiro' e as taxas
# de impostos são as seguintes para os cidadãos com as rendas:
#
# até 1000 dinheiros = 5% de imposto
# entre 1000 e 5000 = 5% sobre 1000 dinheiros e mais 10% sobre o restante
# acima de 5000 = 5% sobre 1000, 10% sobre 4000 e 20% sobre o restante.
#
#
# Tipos de dados: unidade monetária é 'dinheiro' representado por um número real
# A função recebe a renda do cidadão em 'dinheiro' e retorna o imposto a ser pago
# também em 'dinheiro'.

def calcula_imposto(sal:float)->float:
    '''
    Calcula o imposto de um cidadão dado o seu salário de acordo
    com as normas de tributação

    Exemplos:

    >>> calcula_imposto(500)
    25.0

    >>> calcula_imposto(1700)
    120.0

    >>> calcula_imposto(3400)
    290.0

    >>> calcula_imposto(7800)
    1010.0
    '''
    imposto:float = 0
    
    if sal < 1000:
        imposto = sal*0.05

    elif sal >= 1000 and sal < 5000:
        imposto = (1000 * 0.05) + ((sal - 1000) * 0.1)

    else:
        imposto = (1000 * 0.05) + (4000 * 0.1) + ((sal - 5000) * 0.2)

    return imposto
