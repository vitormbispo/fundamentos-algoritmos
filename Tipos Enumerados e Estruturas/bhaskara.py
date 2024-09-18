# Análise:
#
# Projetar uma função que calcule o valor de delta
# com base nos coeficientes a, b e c e depois fazer uma função que diga
# quantas e quais são as raízes da equação
# 
# Tipos de dados: números reais

def calcular_delta(a:float ,b:float,c:float)->float:
    '''
    Calcula o valor de delta

    Exemplos:

    '''

    return (b**2)-4*(a*c)

def bhaskara(a:float, b:float, c:float):
    '''
    Calcula as raízes de uma equação de 2° grau
    '''

    delta = calcular_delta(a,b,c)

    if delta < 0:
        print("Não existe raiz real")
    else:
        if delta == 0:
            print("Existe uma raiz real")
            
            x1 = (-b + (delta**(1/2)))/(2*a)
            print("x1 = "+x1)
        elif delta > 0:
            print("Existem 2 raizes reais")
            x1 = (-b + (delta**(1/2)))/(2*a)
            x2 = (-b - (delta**(1/2)))/(2*a)

            print("x1 = "+str(x1)+" x2 = "+str(x2))
