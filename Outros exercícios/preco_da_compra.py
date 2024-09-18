# Análise
#
# Recebe o código de um produto e a quantidade comprada deste produto
# então calcula o valor total da compra de acordo com a tabela de preços:
#
#
# Código    |   Preço
# 1001          5,32
# 1324          6,45
# 6548          2,37
# 2987          5,32
# 7623          6,45

def preco_da_compra(produto:str, quantidade:int) -> float:
    '''
    Calcula o preço total da compra de um 'produto' em 'quantidade'

    Exemplos:

    >>> preco_da_compra('1324',2)
    12.9

    >>> preco_da_compra('2987',7)
    37.24
    '''
    preco_und: float = 0.0

    if produto == '1001':
        preco_und = 5.32

    if produto == '1324':
        preco_und = 6.45

    if produto == '6548':
        preco_und = 2.37

    if produto == '2987':
        preco_und = 5.32

    if produto == '7623':
        preco_und = 6.45
    
    return preco_und * quantidade
