'''
Autor: Vitor Martins Bispo RA138475

Análise: projetar um algoritmo que utilize uma matriz com os dados das medalhas
concedidas nos Jogos Olímpicos de Paris 2024 para montar o quadro de medalhas dos jogos
em ordem de classificação, sendo os maiores classificados aqueles com maior quantidade de medalhas de ouro
com desempate decidido pela quantidade de medalhas de prata ou bronze.
Após o quadro de medalhas, exibir uma lista com os países que tiveram apenas atletas de um único gênero
contemplados com medalhas utilizando recursividade.

Tipos de dados: as informações das medalhas são uma matriz de strings oferecida como parâmetro na
linha de comando na execução do programa que será a entrada principal de dados do programa. 
A matriz deve ser transformada em uma lista de tipos estruturados.
Os dados de cada país também devem ser armazenados em um tipo estruturado.
Dados como gênero e tipos de medalhas devem ser representadas por tipos enumerados.
Como saída, o programa exibe o quadro de medalhas e a lista de países com atletas de
um único gênero no terminal.
'''

import sys
from dataclasses import dataclass
from enum import Enum, auto

# - TIPOS ENUMERADOS
class TipoDeMedalhas(Enum):
    OURO = 1
    PRATA = 2
    BRONZE = 3

class Genero(Enum):
    W = auto()
    M = auto()
    X = auto()
    O = auto()

class Indices(Enum): # - Os valores são equivalentes aos índices de cada informação na matriz da tabela.
    TIPO = 1
    GENERO = 4
    PAIS = 10

# - TIPOS ESTRUTURADOS
@dataclass
class Medalha():
    tipo:TipoDeMedalhas
    genero:Genero
    pais:str = ""

@dataclass
class Pais():
    medalhas:list[Medalha]
    contagem_medalhas:list[int] # - Indices: 0 = Ouro. 1 = Prata. 2 = Bronze
    pais:str = "" 
    total_medalhas:int = 0
    classificacao:int = 0


def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    tabela = le_arquivo(sys.argv[1])

     # TODO: computar e exibir o quadro de medalhas
    paises:list[Pais] = criar_lista_paises(tabela) # - Transforma e separa os dados das medalhas para cada país

    organizar_por_classificacao(paises) # - Ordena

    print(montar_tabela(paises)) # - Exibe o quadro de medalhas
    print(len(paises), "Paises contemplados")

    print("\n __________________________________________________________________ \n") # Separação
    
    # TODO: computar e exibir os países que tiverem apenas
    # atletas de um único gênero premiados
    paises_genero:list[Pais] = paises_apenas_um_genero(paises)

    print("- Lista de países com atletas de apenas um gênero: ")
    exibir_paises(paises_genero)


def criar_lista_paises(medalhas:list[list:str]) -> list[Pais]:
    '''
    Transforma cada informação de medalha na matriz de strings 'medalhas' em
    uma estrutura do tipo 'Medalha'. Em seguida, tal medalha é contabilizada
    para o país que pertence e adicionada a uma lista de estruturas do tipo 'Pais' 
    que será o retorno da função.

    Exemplos de conversão de matriz para 'Medalha':
    ['1','W',"BRA"]
    Medalha(tipo=TipoDeMedalha.OURO, genero=Genero.W, pais="BRA"))

    ['3','X','CHN']
    Medalha(tipo=TipoDeMedalha.BRONZE, genero=Genero.M, pais="CHN"))

    Exemplo de conversão de 'Medalha' para 'Pais':
    
    medalhas = [Medalha(tipo=TipoDeMedalha.OURO,pais="BRA"),Medalha(tipo=TipoDeMedalha.OURO,pais="BRA"),Medalha(tipo=TipoDeMedalha.PRATA,pais="BRA")]
    Pais(medalhas = medalhas,contagem_medalhas=[2,1,0],pais="BRA",total=3,classificacao=1)
    '''

    paises:list[Pais] = []
    for medalha in medalhas:
        nova_medalha:Medalha = Medalha(medalha[Indices.TIPO.value],medalha[Indices.GENERO.value],medalha[Indices.PAIS.value])
            
        # - Converter as strings para um tipo enumerado:
        nova_medalha.tipo = TipoDeMedalhas(int(nova_medalha.tipo))
        nova_medalha.genero = Genero[nova_medalha.genero]

        # - Contabilizar medalha ao país
        if indice_do_pais(nova_medalha.pais,paises) == -1: # - País não existe na lista, adicionando...
            novo_pais:Pais = Pais([nova_medalha],[0,0,0],nova_medalha.pais,1)
            novo_pais.contagem_medalhas[nova_medalha.tipo.value-1] = 1 # - Código da medalha -1 = índice na lista de contagem de medalhas

            paises.append(novo_pais)

        else: # - Pais existe. Adicionando medalha...
            pais:Pais = paises[indice_do_pais(nova_medalha.pais,paises)]

            pais.medalhas.append(nova_medalha)
            pais.contagem_medalhas[nova_medalha.tipo.value-1] = pais.contagem_medalhas[nova_medalha.tipo.value-1] + 1 # - Código da medalha -1 = índice na lista de contagem de medalhas
            pais.total_medalhas = pais.total_medalhas + 1
    return(paises)

def organizar_por_classificacao(paises:list[Pais]):
    '''
    Organiza a lista de 'paises' por ordem de classificação.
    A classificação é definida de acordo com a quantidade de medalhas de ouro: quanto mais medalhas, mais alta.
    O desempate é feito por medalhas de prata e, persistindo o empate, por medalhas de bronze.
    Esta função não tem retorno, ela modifica a lista 'paises'.

    Exemplos:
    
    >>> pais1 = Pais(pais="ARG",contagem_medalhas=[3,0,2],medalhas=[])
    >>> pais2 = Pais(pais="EUA",contagem_medalhas=[40,10,10],medalhas=[])
    >>> pais3 = Pais(pais="SWE",contagem_medalhas=[3,0,3],medalhas=[])
    >>> pais4 = Pais(pais="BRA",contagem_medalhas=[3,5,6],medalhas=[])
    
    >>> paises = [pais1,pais2,pais3,pais4]

    >>> organizar_por_classificacao(paises)
    >>> paises[0].pais
    'EUA'
    >>> paises[1].pais
    'BRA'
    >>> paises[2].pais
    'SWE'
    >>> paises[3].pais
    'ARG'
    '''
    
    j:int = 0
    
    while j < len(paises):
        primeiro = paises[j]
        indice_maior = indice_maior_classificado(paises,j,len(paises))
        paises[j] = paises[indice_maior]
        paises[indice_maior] = primeiro

        paises[j].classificacao = j+1
        j = j + 1


def indice_maior_classificado(paises:list[Pais],i_min:int,i_max:int) -> int:
    '''
    Retorna o índice do pais melhor classificado da lista 'paises'.
    A classificação é feita com base na maior quantiade de medalhas de ouro.
    Em caso de empate, o desempate é por medalhas de prata, persistindo o empate,
    o desempate é feito por medalhas de bronze.

    >>> pais1 = Pais(pais="EUA",contagem_medalhas=[40,10,10],medalhas=[])
    >>> pais2 = Pais(pais="BRA",contagem_medalhas=[3,5,6],medalhas=[])
    >>> pais3 = Pais(pais="SWE",contagem_medalhas=[2,0,1],medalhas=[])
    >>> paises = [pais1,pais2,pais3]
    >>> indice_maior_classificado(paises,0,3)
    0

    >>> pais1 = Pais(pais="ITA",contagem_medalhas=[1,2,2],medalhas=[])
    >>> pais2 = Pais(pais="FRA",contagem_medalhas=[1,5,1],medalhas=[])
    >>> pais3 = Pais(pais="ARG",contagem_medalhas=[1,3,0],medalhas=[])
    >>> indice_maior_classificado([pais1,pais2,pais3],0,3)
    1

    '''
    maior = i_min
    for i in range(i_min,i_max):
        if paises[i].contagem_medalhas[0] > paises[maior].contagem_medalhas[0]:
            maior = i

        elif paises[i].contagem_medalhas[0] == paises[maior].contagem_medalhas[0]:
            if paises[i].contagem_medalhas[1] > paises[maior].contagem_medalhas[1]:
                maior = i

            elif paises[i].contagem_medalhas[1] == paises[maior].contagem_medalhas[1]:
                if paises[i].contagem_medalhas[2] > paises[maior].contagem_medalhas[2]:
                    maior = i

    return maior

def indice_do_pais(pais:str,paises:list[Pais]) -> int:
    '''
    Retorna o índice do 'pais' dentro da lista de estruturas 'paises'.
    Retorna -1 caso o 'pais' não exista na lista.

    Exemplos:

    >>> paises = [Pais([],[],pais="EUA"),Pais([],[],pais="BRA"),Pais([],[],pais="ENG"),Pais([],[],pais="CHN")]
    >>> indice_do_pais("BRA", paises)
    1

    >>> indice_do_pais("ENG", paises)
    2

    >>> indice_do_pais("POR", paises)
    -1
    '''
    i:int = 0
    i_pais:int = -1
    
    while i < len(paises) and i_pais == -1:
        if paises[i].pais == pais:
            i_pais = i
        i = i + 1
    return i_pais

def montar_tabela(paises:list[Pais]) -> str:
    '''
    Monta uma tabela de classificação dos 'paises' exibindo:
    sigla do país; quantidade de medalhas de ouro, prata e bronze;
    quantidade total de medalhas; e classificação.
    A tabela é dada como uma string.

    Exemplo de saída:

_________________________________________________

| QUADRO DE MEDALHAS | OLIMPÍADAS DE PARIS 2024 |
_________________________________________________
| País | Ouro | Prata | Bronze | Total | Clas.  |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
| BRA  | 10   | 15    | 12     | 37    | 1      |
| FRA  | 12   | 13    | 15     | 40    | 2      |
| ARG  | 18   | 19    | 16     | 53    | 3      |
| AUS  | 14   | 22    | 29     | 65    | 4      |
| BEL  | 3    | 1     | 6      | 10    | 5      |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

    '''

    tabela:str = '''
_________________________________________________

| QUADRO DE MEDALHAS | OLIMPÍADAS DE PARIS 2024 |
_________________________________________________
| País | Ouro | Prata | Bronze | Total | Clas.  |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
'''

    for pais in paises:
        linha:str = "| "
        
        linha = linha + str(pais.pais + "  | ") # - País    
        
        # Para padronizar o espaço, reduz a quantidade de espaços a serem adicionados de acordo com o tamanho do número
        # Fórmula: ' ' * 'espaçamento desejado' - 'tamanho do número'
        linha = linha + str(pais.contagem_medalhas[0]) + ' '*(5-len(str(pais.contagem_medalhas[0])))+'| ' # - Medalhas de ouro
        linha = linha + str(pais.contagem_medalhas[1]) + ' '*(6-len(str(pais.contagem_medalhas[1])))+'| ' # - Medalhas de prata
        linha = linha + str(pais.contagem_medalhas[2]) + ' '*(7-len(str(pais.contagem_medalhas[2])))+'| ' # - Medalhas de bronze
        linha = linha + str(pais.total_medalhas) + ' '*(6-len(str(pais.total_medalhas)))+'| '             # - Total
        linha = linha + str(pais.classificacao) + ' '*(7-len(str(pais.classificacao)))+'|\n'              # - Classificação

        tabela = tabela + linha

    tabela += '‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'

    return tabela

def possui_apenas_um_genero(medalhas:list[Medalha],i:int = 0,genero = Genero.M) -> bool:
    '''
    Checa se na lista de 'medalhas' existem apenas atletas do mesmo 'genero', 
    desconsiderando países venceram em categorias mistas.
    Retorna o 'resultado' verdadeiro ou falso e usa 'i' como índice da lista.

    Exemplos:
    >>> m = [Medalha(TipoDeMedalhas.OURO,Genero.W,"BRA"),Medalha(TipoDeMedalhas.PRATA,Genero.W,"BRA"),Medalha(TipoDeMedalhas.OURO,Genero.W,"BRA")]
    >>> possui_apenas_um_genero(m)
    True

    >>> m = [Medalha(TipoDeMedalhas.PRATA,Genero.W,"EUA"),Medalha(TipoDeMedalhas.BRONZE,Genero.M,"EUA"),Medalha(TipoDeMedalhas.OURO,Genero.M,"OURO")]
    >>> possui_apenas_um_genero(m)
    False

    >>> m = [Medalha(TipoDeMedalhas.BRONZE,Genero.O,"AUS"),Medalha(TipoDeMedalhas.BRONZE,Genero.O,"AUS"),Medalha(TipoDeMedalhas.PRATA,Genero.O,"AUS")]
    >>> possui_apenas_um_genero(m)
    False
    '''
    if(i == 0): # - Primeira iteração
        genero = medalhas[0].genero # - Fixar genero
        resultado:bool = True
    
    if genero != Genero.O and Genero.X: # - Excluindo paises que ganharam competições mistas
        if(i >= len(medalhas)): # - Caso base
            resultado = True

        elif medalhas[i].genero == genero:
            resultado = possui_apenas_um_genero(medalhas,i+1,genero)
        
        else:
            resultado = False
    else:
        resultado = False
    
    return resultado


def paises_apenas_um_genero(paises:list[Pais],i:int = 0,lista:list[Pais] = []) -> list[Pais]:
    '''
    Retorna uma lista com os 'paises' que possuem apenas atletas de um
    mesmo gênero, utilizando 'i' como índice e 'lista' como retorno.

    Exemplos:

    >>> mPais1 = [Medalha(TipoDeMedalhas.OURO,Genero.W,"BRA"),Medalha(TipoDeMedalhas.PRATA,Genero.W,"BRA"),Medalha(TipoDeMedalhas.OURO,Genero.W,"BRA")]
    >>> mPais2 = [Medalha(TipoDeMedalhas.PRATA,Genero.W,"EUA"),Medalha(TipoDeMedalhas.BRONZE,Genero.M,"EUA"),Medalha(TipoDeMedalhas.OURO,Genero.M,"OURO")]
    >>> mPais3 = [Medalha(TipoDeMedalhas.BRONZE,Genero.O,"AUS"),Medalha(TipoDeMedalhas.BRONZE,Genero.O,"AUS"),Medalha(TipoDeMedalhas.PRATA,Genero.O,"AUS")]
    
    >>> paises = [Pais(mPais1,[],"BRA"),Pais(mPais2,[],"EUA"),Pais(mPais3,[],"AUS")]
    >>> paises_apenas_um_genero(paises)[0].pais
    'BRA'
    
    '''
    if i >= len(paises) - 1: # - Caso base
        if possui_apenas_um_genero(paises[len(paises) - 1].medalhas):
            lista.append(paises[len(paises) - 1])
    else:
        if possui_apenas_um_genero(paises[i].medalhas):
            lista.append(paises[i])
        paises_apenas_um_genero(paises,i+1,lista)
    
    return lista

def exibir_paises(paises:list[Pais],i:int = 0):
    ''' 
    Exibe a sigla dos 'paises' no terminal.
    'i' é o índice e é iniciado em 0.
    Função sem retorno.

    Exemplos:
    >>> paises = [Pais([],[],pais="EUA"),Pais([],[],pais="BRA"),Pais([],[],pais="ENG"),Pais([],[],pais="CHN")]
    >>> exibir_paises(paises)
      - EUA
      - BRA
      - ENG
      - CHN

    >>> paises = [Pais([],[],pais="ARG"),Pais([],[],pais="ITA"),Pais([],[],pais="POL"),Pais([],[],pais="DEN")]
    >>> exibir_paises(paises)
      - ARG
      - ITA
      - POL
      - DEN
    '''

    if i >= len(paises) - 1:
        print("  -",paises[i].pais)
    else:
        print("  -",paises[i].pais)
        exibir_paises(paises, i+1)
        
def le_arquivo(nome: str) -> list[list[str]]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é
    uma lista com os valores das colunas de uma linha (valores separados por
    vírgula). A primeira linha do arquivo, que deve conter o nome das
    colunas, é descartado.
    Por exemplo, se o conteúdo do arquivo for
    tipo,cor,ano
    carro,verde,2010
    moto,branca,1995
    a resposta produzida é
    [['carro', 'verde', '2010'], ['moto', 'branca', '1995']]
    '''
    try:
        with open(nome) as f:
            tabela = []
            linhas = f.readlines()
        for i in range(1, len(linhas)):
            tabela.append(linhas[i].split(','))
        return tabela
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.')
        sys.exit(1)

if __name__ == '__main__':
    main()