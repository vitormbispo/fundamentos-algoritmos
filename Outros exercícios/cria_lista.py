def cria_lista(n:int,v:int,lista = []):
    if n == 1: # Caso base
        lista.append(v)
    else:
        lista.append(v)
        cria_lista(n-1,v,lista)
    
    return lista

def fatorial(n:int):
    fat = 0
    if(n == 1):
        fat = 1
    else:
        fat = n * fatorial(n-1)
    return fat

def um_a_n(n:int,string:str = ""):
    if n <= 1:
        string = string + str(n)
    else:
        string += um_a_n(n-1,string)+", "+str(n)
    
    return string

print(um_a_n(4))

def tem_positivo(lis:list[int],i:int = 0):
    if lis != []:
        if i >= len(lis)-1:
            pos = lis[i] > 0
        else:
            if lis[i] > 0:
                pos = True
            else:
                pos = tem_positivo(lis,i+1)

    else:
        pos = False

    return pos

def matriz_pos(m:list[list[int]],i:int = 0):
    if m != []:
        if i >= len(m) -1:
            pos = tem_positivo(m[i])
        else:
            if tem_positivo(m[i]):
                pos = matriz_pos(m,i+1)
            else:
                pos = False
    else:
        pos = False
    return pos

print(matriz_pos([[1,-4,-4]]))

        