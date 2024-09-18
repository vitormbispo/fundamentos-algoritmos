def grafico_barra(valor:float,total:float) -> str:
    '''
    Retorna um gráfico em formato de barra horizontal representando
    a porcentagem do 'valor' em relação ao 'total'.
    '''
    TAMANHO:int = 20
    porcento:float = valor/total
    barras:int = int(TAMANHO*porcento)

    barra:str = '['+('#'*(barras))+('-'*(TAMANHO-(barras)))+']'
    return barra
