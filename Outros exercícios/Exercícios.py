
def main():
    print("area_retangulo(3.0, 5.0)")
    print(area_retangulo(3.0, 5.0))
    print("")

    print("produto_anterior_posterior(3)")
    print(produto_anterior_posterior(3))
    print("")

    print("aumenta(100.0, 3.0)")
    print(aumenta(100.0, 3.0))
    print("")

    print("zera_dezena_e_unidade(19)")
    print(zera_dezena_e_unidade(19))
    print("")

    print("exclamacao('Nossa', 3)")
    print(exclamacao('Nossa', 3))
    print("")

    print("primeira_maiuscula('joao venceu.')")
    print(primeira_maiuscula('joao venceu.'))
    print("")
    
    print("censura('droga de lanche!', 5)")
    print(censura('droga de lanche!', 5))

def area_retangulo(w:float,h:float): # Multiplca 'w' e 'h'
    return w*h

def produto_anterior_posterior(x:int)->int: # Multiplica 'x' com o inteiro anterior e posterior dele
    return (x-1)*x*(x+1)

def aumenta(n:int,cem:int)->float: # Adiciona +'cem'% a 'n'
    return n+(n*(cem/100))

def zera_dezena_e_unidade(n: float)->float: # Retorna 'n' excluindo as dezenas e unidades
    n = n//100
    n = n*100
    return n

def exclamacao(txt:str,num:int) -> str: # Adiciona 'num' número de "!" ao fim do texto 'txt'
    txt = txt+("!"*num)
    return txt

def primeira_maiuscula(txt:str)->str: # Retorna o texto 'txt' com a primeira letra maiúscula
    txt = txt[0].upper()+txt[1:]
    return txt

def censura(txt:str,num:int)->str: # Censura as 'num' primeiras letras do texto 'txt'
    sem_censura = txt[num:]
    return "x"*num+sem_censura



main()


