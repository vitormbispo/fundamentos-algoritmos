# Autores: Bruno Yozo RA140076 e Vitor Bispo RA138475
#
# Análise
#
# Projetar um sistema de gestão com duas funções principais:
#
# - Registrar uma venda: registra os seguintes dados do usuário que efetuou
# a compra: relação do usuário com a universidade, quantidade de tíquetes, forma de pagamento e total da compra.
# O sistema calcula o valor total da compra baseado nos seguintes valores fixos
# de acordo com a relação do usuário:
#  
#   ALUNO: R$5,00
#   SERVIDOR COM MENOS DE 3 SALÁRIOS: R$5,00
#   SERVIDOR COM MAIS DE 3 SALÁRIOS: R$10,00
#   DOCENTE: R$10,00
#   PESSOA EXTERNA: R$19,00
#
# Após confirmação da venda, fica disponível para registrar outra venda. 
# Armazena cada venda em uma lista com todas as vendas.
#
# - Exibir o relatório de vendas: Exibe a quantidade total de tíquetes vendidos,
# a receita total registrada, e dois gráficos em barras mostrando a porcentagem
# de vendas para cada tipo de usuário e a porcentagem da receita gerada
# por cada forma de pagamento.
#
#
# Tipos de dados:
# 
# Entradas principais recebidas pelo usuário como strings na função de registro.
#
# Representar vendas como um tipo estruturado contendo: tipo de usuário como
# tipo enumerado; Forma de pagamento como tipo enumerado; Quantidade de tíquetes
# como número inteiro e valor total da compra como número real.
#
# Lista de vendas como uma lista contendo itens do tipo estruturado das vendas.
#
# Estatísticas a serem exibidas como um tipo estruturado para armazenar os dados e cálculos relevantes.
#
# Saída principal na função do relatório, exibindo as informações e gráficos como strings.

# - Import
from enum import Enum, auto
from dataclasses import dataclass

# - Tipos enumerados:
class TipoDeUsuario(Enum):
        ALUNO = auto()
        SERVIDOR = auto()
        SERVIDOR_3 = auto()
        DOCENTE = auto()
        PESSOA_EXTERNA = auto()

class FormaDePagamento(Enum):
    DINHEIRO = auto()
    CARTAO = auto()
    PIX = auto()

# - Tipos estruturados
@dataclass
class Venda():
    tipo_usuario:TipoDeUsuario
    pagamento:FormaDePagamento
    quantidade:int
    valor:float

@dataclass
class Estatisticas():
    aluno_quant:int = 0         # Quantidade de tickets dos alunos
    servidor_quant:int = 0      # Quantidade de tickets dos servidores com menos de 3 salários
    servidor3_quant:int = 0     # Quantidade de tickets dos servidores com mais de 3 salários
    docente_quant:int = 0       # Quantidade de tickets dos docentes
    externa_quant:int = 0       # Quantidade de tickets da comunidade externa
    total_quant:int = 0         # Quantidade total de tickets

    cartao_rec:float = 0        # Receita das vendas no cartão
    dinheiro_rec:float = 0      # Receita das vendas no dinheiro
    pix_rec:float = 0           # Receita das vendas no pix
    total_rec:float = 0         # Receita total   

#
# - FUNÇÕES INICIAIS
#
def inicio():        
    lista:list[Venda] = [] # Inicializa a lista de vendas.
    boas_vindas() # Mensagem
    sistema(lista)  # Inicializa o sistema

def boas_vindas():
    '''
    Exibe uma mensagem de boas vindas para o usuário.
    '''

    print('''
#=================================================================================#
                                              __
                                             / /
                                            / /
                        \\‾‾‾\\      /\\      / /  
                         \\   \\    / /     / / /‾‾‾‾‾|
                          \\   \\  / /  /\\  \\ \\ \\_____|
                           \\__/ / /  /  \\  \\ \\ 
                      _________/ /  /    \\  \\ \\ 
                      \\_________/   ‾‾‾‾‾‾   \\ \\ 
                                 /‾‾‾‾‾‾‾‾‾\\  ‾‾            
                                 ‾‾‾‾‾‾‾‾‾\\ \\ 
                                      /‾‾\\ \\ \\ 
                                     /   /  \\ \\ 
                                    /   /    \\|
                                    ‾‾‾‾ 
#================================================================================#

              |‾‾‾|     |   |         |         |   |   |‾‾‾  |\\  /| 
              |___|     |   |       -----       |   |   |---  | \\/ | 
#============ |   \\  .  |___|         |         |___|   |___  |    | ============#

               Seja bem vindo(a) ao sistema de gestão do RU da UEM!
     
#================================================================================#
''')

def sistema(lista:list[Venda]): # -> Função do sistema.
    '''
    Função principal do sistema. Inicializa um menu de opções
    para o usuário iniciar a navegação pelo sistema incluindo as funções
    disponíveis 'registrar' e 'consultar_historico' e carregando a 'lista' de vendas
    para cada função. O usuário também pode encerrar o programa
    com a opção 'sair'
    '''

    # - Separação
    print('''
#===============================================================================================================#
    
    - MENU PRINCIPAL:   
          ''')
    
    sair = False
    while not sair:
        
        funcao = input('Registrar uma venda (1), exibir um relatório das vendas (2) ou sair (3) ? ')

        if funcao == ('1'):
            registrar(lista) # -> Chama a função de registro.
           # sair = True
        
        elif funcao == ('2'):
            consultar_historico(lista)
           # sair = True
        
        elif funcao == ('3'):
           sair = True  

#   
# FUNÇÕES PRINCIPAIS (Entrada e saída principais):
#
def registrar(lista:list[Venda]): # - Entrada principal de dados.
    '''
    Registra uma nova venda com base nas entradas do usuário.
    Em uma venda são registrados o tipo do usuário, a quantidade de tíquetes comprados
    a forma de pagamento e o total da compra. Após a coleta dos dados, inclui a
    venda na 'lista' de vendas
    '''
    
    # - Separação
    print('''
#===============================================================================================================#
    
    - REGISTRAR VENDA:   
          ''')

    
    entrada_valida:bool = False # - Checagem de entrada
    while not entrada_valida:
        tipo:str = (input(' - Você é SERVIDOR, ALUNO, DOCENTE, ou PESSOA_EXTERNA ? ')).upper() # - Tipo de Usuário
        
        renda = 0
            
        if tipo == 'SERVIDOR' :
            renda = float(input(' - Qual a sua renda mensal em R$ ? (Utilize apenas números positivos. Ex.: 1234.56) ')) # - Renda (Apenas se for servidor)
            
            SALARIO_MINIMO = 1412.0 # - Valor do salário mínimo.
            
            if(renda > 3 * SALARIO_MINIMO): # - Se renda do servidor maior que 3 salários:
                tipo = 'SERVIDOR_3' # - Tipo = Servidor acima de 3 salários.
    
        if(verificar_entrada(tipo,TipoDeUsuario)): # - Verificação de entrada
            entrada_valida = True
        else:
            print('\n---  /!\\ ENTRADA INVÁLIDA. Tente novamente. ---\n') # - Feedback
        

    quantidade = int(input(' - Quantos tíquetes serão comprados? (Utilize apenas números naturais) '))


    entrada_valida = False # - Checagem
    while not entrada_valida:
        forma_pagamento = str(input(' - CARTAO, DINHEIRO ou PIX ? ' )).upper()
        
        if(verificar_entrada(forma_pagamento,FormaDePagamento)): # - Verificação
            entrada_valida = True
        else:
            print('\n---  /!\\ ENTRADA INVÁLIDA. Tente novamente. ---\n') # - Feedback
    
    total = calcular_valor(TipoDeUsuario[tipo], quantidade) # - Valor total da venda

    print('\n # - O total da compra foi de: R$'+str(total)+' - #')

        
    entrada_valida = False # - Checagem de entrada.
    while not entrada_valida:       
        confirmar = str(input('\n - Confirmar venda? (S/N) ')).upper() # - Confirmação do pedido
        if confirmar == 'S': # - Venda registrada.
            nova_venda:Venda = Venda(TipoDeUsuario[tipo],FormaDePagamento[forma_pagamento],quantidade,total) # - Cria a nova venda
            lista.append(nova_venda) # Adiciona o valor das venda à lista.
            
            print("\n---Venda registrada!---\n")
            entrada_valida = True
        elif confirmar == 'N':
            print("\n---Venda cancelada.---\n")
            entrada_valida = True
        
        else: # - Entrada inválida
           print('\n---  /!\\ ENTRADA INVÁLIDA. Tente novamente. ---\n') # - Feedback  
    
    
    entrada_valida = False # - Checagem de entrada.
    while not entrada_valida:
        nova = input(" - Registrar nova venda? (S/N) ").upper() # - Continuar registrando:
        if nova == 'S':
            entrada_valida = True
            registrar(lista)          
        elif nova == 'N':
            entrada_valida = True
            sistema(lista)
        else:  # - Entrada inválida.
            print('\n---  /!\\ ENTRADA INVÁLIDA. Tente novamente. ---\n') # - Feedback

def consultar_historico(lista:list[Venda]): # - Saída principal de dados ao usuário.
    '''
    Consulta o histórico de vendas armazenadas na 'lista', exibindo receita, total de tickets vendidos e
    dois gráficos de barras: o primeiro mostra a relação de vendas por tipo de usuário e o 
    segundo a relação da receita com a forma de pagamento.
    '''

    # - Separação
    print('''
#===============================================================================================================#
    
    - RELATÓRIO DE VENDAS:   
          ''')
    
    if lista == []: # Caso não tenha vendas registradas
        print("\n Nenhuma venda registrada. \n")
        sistema(lista)
    
    else: 
        estat = calcular_estatisticas(lista) # - Gerar as estatísticas do dia
   
        print(f' - A receita de hoje foi: {estat.total_rec}')
        print(f' - A venda total de tickets foi: {estat.total_quant}')
   
        grafico_tickets_por_usuario(estat)
        grafico_receita_por_pagamento(estat)
        sistema(lista)

#
# FUNÇÕES INTERMEDIÁRIAS (Cálculos, operações e verificações)
#
def verificar_entrada(entrada:str,tipo:Enum) -> bool:
    '''
    Verifica se a 'entrada' como 'str' pertence ao 'tipo' ENUMERADO.

    Exemplos:

    >>> verificar_entrada('ALUNO',TipoDeUsuario)
    True

    >>> verificar_entrada('DINHEIRO',FormaDePagamento)
    True

    >>> verificar_entrada('SERVIDOR_3',TipoDeUsuario)
    True

    >>> verificar_entrada('SERVIDOR',FormaDePagamento)
    False

    >>> verificar_entrada('asd',TipoDeUsuario)
    False
    '''
    valido = False
    
    for item in tipo: # - Verificação de entrada    
        if item.name == entrada:
            valido = True

    return valido

#
# Cálculos para estatísticas
#
def calcular_valor(tipo:TipoDeUsuario,quantidade:int) -> float:
    '''
    Calcula o valor total de uma compra, baseada no 'tipo' do usuario e 'quantidade' de tíquetes comprados.

    Exemplos:

    >>> calcular_valor(TipoDeUsuario.ALUNO,5)
    25.0

    >>> calcular_valor(TipoDeUsuario.SERVIDOR, 2)
    10.0

    >>> calcular_valor(TipoDeUsuario.SERVIDOR_3, 2)
    20.0
    
    >>> calcular_valor(TipoDeUsuario.DOCENTE,5)
    50.0
    '''
    preco:float = 0.0

    if tipo == TipoDeUsuario.ALUNO:
        preco = 5.0
    
    elif tipo == TipoDeUsuario.DOCENTE:
        preco = 10.0
    
    elif tipo == TipoDeUsuario.SERVIDOR: # - Servidor com menos de 3 salários
        preco = 5.0
    
    elif tipo == TipoDeUsuario.SERVIDOR_3: # - Servidor com mais de 3 salários
        preco = 10.0

    elif tipo == TipoDeUsuario.PESSOA_EXTERNA:
        preco = 19.0
    
    valor:float = quantidade * preco

    return valor

def calcular_tickets(lista:list[Venda]) -> int:
    '''
    Calcula a quantidade de tíquetes totais comprados até agora em todas as vendas da 'lista'.

    Exemplos:
    >>> venda1:Venda = Venda(TipoDeUsuario['SERVIDOR'],FormaDePagamento['PIX'],5,25)
    >>> venda2:Venda = Venda(TipoDeUsuario['ALUNO'],FormaDePagamento['DINHEIRO'],3,15)
    >>> venda3:Venda = Venda(TipoDeUsuario['DOCENTE'],FormaDePagamento['CARTAO'],2,20)
    >>> lista:list[Venda] = [venda1,venda2,venda3]
    >>> calcular_tickets(lista)
    10

    >>> venda1:Venda = Venda(TipoDeUsuario['DOCENTE'],FormaDePagamento['DINHEIRO'],3,30)
    >>> venda2:Venda = Venda(TipoDeUsuario['PESSOA_EXTERNA'],FormaDePagamento['PIX'],2,38)
    >>> venda3:Venda = Venda(TipoDeUsuario['SERVIDOR_3'],FormaDePagamento['CARTAO'],4,40)
    >>> lista:list[Venda] = [venda1,venda2,venda3]
    >>> calcular_tickets(lista)
    9
    '''

    total:int = 0
    
    for venda in lista:
        total += venda.quantidade
    
    return total

def calcular_receita(lista:list[Venda]) -> float:
    '''
    Calcula a receita total das vendas até agora em todas as vendas da 'lista'.

    Exemplos:
    >>> venda1:Venda = Venda(TipoDeUsuario['SERVIDOR'],FormaDePagamento['PIX'],5,25)
    >>> venda2:Venda = Venda(TipoDeUsuario['ALUNO'],FormaDePagamento['DINHEIRO'],3,15)
    >>> venda3:Venda = Venda(TipoDeUsuario['DOCENTE'],FormaDePagamento['CARTAO'],2,20)
    >>> lista:list[Venda] = [venda1,venda2,venda3]
    >>> calcular_receita(lista)
    60

    >>> venda1:Venda = Venda(TipoDeUsuario['DOCENTE'],FormaDePagamento['DINHEIRO'],3,30)
    >>> venda2:Venda = Venda(TipoDeUsuario['PESSOA_EXTERNA'],FormaDePagamento['PIX'],2,38)
    >>> venda3:Venda = Venda(TipoDeUsuario['SERVIDOR_3'],FormaDePagamento['CARTAO'],4,40)
    >>> lista:list[Venda] = [venda1,venda2,venda3]
    >>> calcular_receita(lista)
    108
    '''

    receita:float = 0

    for venda in lista:
        receita += venda.valor
    
    return receita

def tickets_por_tipo(lista:list[Venda],tipo:TipoDeUsuario):
    '''
    Calcula o número total de tickets na 'lista' de vendas por 'tipo' de usuário.
    
    Exemplos:
    >>> venda1:Venda = Venda(TipoDeUsuario['ALUNO'],FormaDePagamento['PIX'],5,25)
    >>> venda2:Venda = Venda(TipoDeUsuario['ALUNO'],FormaDePagamento['DINHEIRO'],3,15)
    >>> venda3:Venda = Venda(TipoDeUsuario['DOCENTE'],FormaDePagamento['CARTAO'],2,20)
    >>> lista:list[Venda] = [venda1,venda2,venda3]
    >>> tickets_por_tipo(lista,TipoDeUsuario.ALUNO)
    8

    >>> venda1:Venda = Venda(TipoDeUsuario['PESSOA_EXTERNA'],FormaDePagamento['CARTAO'],5,25)
    >>> venda2:Venda = Venda(TipoDeUsuario['ALUNO'],FormaDePagamento['DINHEIRO'],3,15)
    >>> venda3:Venda = Venda(TipoDeUsuario['DOCENTE'],FormaDePagamento['DINHEIRO'],2,20)
    >>> lista:list[Venda] = [venda1,venda2,venda3]
    >>> tickets_por_tipo(lista,TipoDeUsuario.SERVIDOR)
    0

    >>> lista:list[Venda] = []
    >>> tickets_por_tipo(lista,TipoDeUsuario.DOCENTE)
    0
    '''

    total = 0

    for venda in lista:
        if venda.tipo_usuario == tipo:
            total = total + venda.quantidade
    
    return total

def receita_por_pagamento(lista:list[Venda],pagamento:FormaDePagamento):
    '''
    Calcula a receita total de determinado tipo de 'pagamento'
    nas vendas da 'lista'.
    
    Exemplos:
    >>> venda1:Venda = Venda(TipoDeUsuario['ALUNO'],FormaDePagamento['PIX'],5,25)
    >>> venda2:Venda = Venda(TipoDeUsuario['ALUNO'],FormaDePagamento['DINHEIRO'],3,15)
    >>> venda3:Venda = Venda(TipoDeUsuario['DOCENTE'],FormaDePagamento['PIX'],2,20)
    >>> lista:list[Venda] = [venda1,venda2,venda3]
    >>> receita_por_pagamento(lista,FormaDePagamento.PIX)
    45.0

    >>> venda1:Venda = Venda(TipoDeUsuario['PESSOA_EXTERNA'],FormaDePagamento['CARTAO'],5,25)
    >>> venda2:Venda = Venda(TipoDeUsuario['ALUNO'],FormaDePagamento['DINHEIRO'],3,15)
    >>> venda3:Venda = Venda(TipoDeUsuario['DOCENTE'],FormaDePagamento['DINHEIRO'],2,20)
    >>> lista:list[Venda] = [venda1,venda2,venda3]
    >>> receita_por_pagamento(lista,FormaDePagamento.PIX)
    0.0

    >>> lista:list[Venda] = []
    >>> receita_por_pagamento(lista,FormaDePagamento.DINHEIRO)
    0.0
    '''

    total = 0.0

    for venda in lista:
        if venda.pagamento == pagamento:
            total = total + venda.valor
    
    return total

def calcular_estatisticas(lista:list[Venda]) -> Estatisticas:
    '''
    Calcula as estatísticas a serem exibidas com base na 'lista' de vendas totais
    e armazena em um tipo estruturado 'Estatisticas'.

    Exemplos:
    >>> venda1:Venda = Venda(TipoDeUsuario['SERVIDOR'],FormaDePagamento['PIX'],5,25)
    >>> venda2:Venda = Venda(TipoDeUsuario['ALUNO'],FormaDePagamento['DINHEIRO'],3,15)
    >>> venda3:Venda = Venda(TipoDeUsuario['DOCENTE'],FormaDePagamento['CARTAO'],2,20)
    >>> lista:list[Venda] = [venda1,venda2,venda3]
    >>> calcular_estatisticas(lista)
    Estatisticas(aluno_quant=3, servidor_quant=5, servidor3_quant=0, docente_quant=2, externa_quant=0, total_quant=10, cartao_rec=20.0, dinheiro_rec=15.0, pix_rec=25.0, total_rec=60)
    
    >>> venda1:Venda = Venda(TipoDeUsuario['DOCENTE'],FormaDePagamento['DINHEIRO'],3,30)
    >>> venda2:Venda = Venda(TipoDeUsuario['PESSOA_EXTERNA'],FormaDePagamento['PIX'],2,38)
    >>> venda3:Venda = Venda(TipoDeUsuario['SERVIDOR_3'],FormaDePagamento['CARTAO'],4,40)
    >>> lista:list[Venda] = [venda1,venda2,venda3]
    >>> calcular_estatisticas(lista)
    Estatisticas(aluno_quant=0, servidor_quant=0, servidor3_quant=4, docente_quant=3, externa_quant=2, total_quant=9, cartao_rec=40.0, dinheiro_rec=30.0, pix_rec=38.0, total_rec=108)
    '''
    
    estat:Estatisticas = Estatisticas() # - Nova estatística

    estat.total_quant = calcular_tickets(lista)
    estat.aluno_quant = tickets_por_tipo(lista,TipoDeUsuario.ALUNO)
    estat.docente_quant = tickets_por_tipo(lista,TipoDeUsuario.DOCENTE)
    estat.servidor_quant = tickets_por_tipo(lista, TipoDeUsuario.SERVIDOR)
    estat.servidor3_quant = tickets_por_tipo(lista, TipoDeUsuario.SERVIDOR_3)
    estat.externa_quant = tickets_por_tipo(lista, TipoDeUsuario.PESSOA_EXTERNA)
    
    estat.dinheiro_rec = receita_por_pagamento(lista,FormaDePagamento.DINHEIRO)
    estat.cartao_rec = receita_por_pagamento(lista,FormaDePagamento.CARTAO)
    estat.pix_rec = receita_por_pagamento(lista,FormaDePagamento.PIX)
    estat.total_rec = calcular_receita(lista)

    return estat

#
# Funções dos gráficos
#
def calcular_porcentagem(valor:float,total:float) -> float:
    '''
    Calcula a porcentagem de 'valor' em relação ao 'total'

    Exemplos:

    >>> calcular_porcentagem(10,100)
    10.0

    >>> calcular_porcentagem(40,80)
    50.0

    >>> calcular_porcentagem(5,20)
    25.0
    '''
    return (valor*100)/total

def gerar_grafico(valor:float,total:float) -> str:
    '''
    Constrói um gráfico em barras na horizontal representando
    a porcentagem do 'valor' em relação ao 'total'.

    Exemplos:

    >>> gerar_grafico(1,10)
    '[==]                   10%'

    >>> gerar_grafico(5,20)
    '[=====]                25%'

    >>> gerar_grafico(50,50)
    '[====================] 100%'

    >>> gerar_grafico(0,100)
    '[]                     0%'

    '''
    TAMANHO = 20 # - O TAMANHO equivale a quantidade máxima de '=' no gráfico (quando for 100%)
    porcentagem = calcular_porcentagem(valor,total)
    quantidade:int = int((porcentagem/100)*TAMANHO)

    #                                                V - Padronizar espaçamento da porcentagem.
    grafico = '[' + '='*quantidade +']' + ' '*(TAMANHO-quantidade+1) + str(round(porcentagem))+'%'

    return grafico

def grafico_tickets_por_usuario(estat:Estatisticas):
    '''
    Exibe um gráfico horizontal com a porcentagem de tickets comprados
    por cada tipo de usuário usando caracteres ASCII a partir dos dados
    na estrutura 'estat'.
    '''
    
    barra_aluno = gerar_grafico(estat.aluno_quant,estat.total_quant)
    barra_docente = gerar_grafico(estat.docente_quant,estat.total_quant)
    barra_servidor = gerar_grafico(estat.servidor_quant,estat.total_quant)
    barra_servidor3 = gerar_grafico(estat.servidor3_quant,estat.total_quant)
    barra_externa = gerar_grafico(estat.externa_quant,estat.total_quant)

    print(f'''

    - TICKETS POR TIPO DE USUÁRIO:

            ALUNO          {barra_aluno}
            DOCENTE        {barra_docente}
            SERVIDOR       {barra_servidor}
            SERVIDOR_3     {barra_servidor3}
            PESSOA_EXTERNA {barra_externa}
            ''')
        
def grafico_receita_por_pagamento(estat:Estatisticas):
    '''
    Exibe um gráfico horizontal com a porcentagem de receita gerada
    por cada forma de pagamento usando caracteres ASCII a partir dos dados 
    no tipo estruturado 'estat'.
    '''
    
    barra_dinheiro = gerar_grafico(estat.dinheiro_rec,estat.total_rec)
    barra_cartao = gerar_grafico(estat.cartao_rec,estat.total_rec)
    barra_pix = gerar_grafico(estat.pix_rec,estat.total_rec)

    print(f'''
    
    - RECEITA POR FORMA DE PAGAMENTO:
          
            DINHEIRO       {barra_dinheiro} 
            CARTAO         {barra_cartao}
            PIX            {barra_pix}
        ''')

#------------------------------------------------------------------------------------------------------------------------------#
# Início do programa
inicio()
