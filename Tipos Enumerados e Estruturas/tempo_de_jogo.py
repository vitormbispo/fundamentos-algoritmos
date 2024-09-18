# Análise:
#
# Determinar a duração de um jogo dada seu horário de início e término
#
# Tipos de dados: Horários em horas e minutos como números inteiros

def tempo_de_jogo(inicio_hr:int, inicio_min:int, fim_hr:int, fim_min:int):
    '''
    Determina a duração de um jogo

    Exemplo:
    >>> tempo_de_jogo(9,10,11,10)
    O jogo durou 2 horas e 0 minutos.

    >>> tempo_de_jogo(11,10,9,10)
    O jogo durou 22 horas e 0 minutos.

    >>> tempo_de_jogo(1,50,2,10)
    O jogo durou 0 horas e 20 minutos.

    >>> tempo_de_jogo(12,0,11,59)
    O jogo durou 23 horas e 59 minutos.

    >>> tempo_de_jogo(12,0,12,0)
    O jogo durou 0 horas e 0 minutos.
    
    '''
    
    inicio_em_mins = (inicio_hr*60) + inicio_min
    fim_em_mins = (fim_hr*60) + fim_min

    if(fim_em_mins < inicio_em_mins):
        diferenca = inicio_em_mins - fim_em_mins
        diferenca = (24*60) - diferenca
    else:
        diferenca = fim_em_mins - inicio_em_mins

    horas = diferenca // 60
    minutos = diferenca % 60
    
    print("O jogo durou "+str(horas)+" horas e "+str(minutos)+" minutos.")

        
