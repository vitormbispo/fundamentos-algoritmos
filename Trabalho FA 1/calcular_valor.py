from enum import Enum, auto
# - Tipos:
class TipoDeUsuario(Enum): # -> Tipos já declarados no início do código
        ALUNO = auto()
        SERVIDOR = auto()
        DOCENTE = auto()
        PESSOA_EXTERNA_A_FACULDADE = auto() # --- Dá pra resumir só pra PESSOA_EXTERNA se pás
def calcular_valor(tipo:TipoDeUsuario,quantidade:int,renda:float = 0) -> float:               # --- Aqui faltou colocar o valor de entrada e o tipo da saida. Também vai ser bom a gente ter duas entradas: uma pro tipo de usuário e outra pra renda. Daí
    '''
    Calcula o valor total de uma compra, baseada no 'tipo' do usuario, na sua 'renda'(se for um servidor) e quantidade de tíquetes comprados.

    Exemplos:

    >>> calcular_valor(TipoDeUsuario.ALUNO,5)
    25.0

    >>> calcular_valor(TipoDeUsuario.SERVIDOR, 2, 2500.0)
    10.0

    >>> calcular_valor(TipoDeUsuario.SERVIDOR, 2, 4387.28)
    20.0
    
    >>> calcular_valor(TipoDeUsuario.DOCENTE,5)
    50.0

    >>> calcular_valor(TipoDeUsuario.PESSOA_EXTERNA_A_FACULDADE,3)
    57.0
    '''
    SALARIO_MINIMO:float = 1412.0
    preco:float = 5.0

    if tipo == TipoDeUsuario.ALUNO:
        preco = 5.0
    
    elif tipo == TipoDeUsuario.DOCENTE:
        preco = 10.0
    
    elif tipo == TipoDeUsuario.SERVIDOR:
        if renda > 3 * SALARIO_MINIMO:
            preco = 10.0
        else:
            preco = 5.0
    elif tipo == TipoDeUsuario.PESSOA_EXTERNA_A_FACULDADE:
        preco = 19.0
    
    valor:float = quantidade * preco

    return valor
