import subprocess as sp
import platform
from math import sqrt

def frequencia_absoluta(list): 
    result = []
    result.append(list[0])

    for i in range(len(list)): 
        if (i == 0):
            continue 
        
        result.append(list[i] - list[i-1])

    return result

def intervalos(list,n):
    interval = list[1] - list[0]  

    for i in range(n):
        if(i == 0):
            continue

        list.append(list[i]+interval)

    return list

def intervalosToString(list): 
    result = [] 

    for i in range(len(list) - 1): 
        result.append(str(list[i]) + '-' + str(list[i+1])) 

    return result

def media(list):
    result = [] 

    for i in range(len(list)-1):
        result.append((list[i] + list[i+1])/2)

    return result

def mediaXfrequencia(f,m):
    result = [] 

    for i in range(len(f)): 
        result.append(f[i] * m[i])

    return result

def media2Xfrequencia(f,m):
    result = [] 

    for i in range(len(f)): 
        result.append(f[i] * (m[i]**2))

    return result

def printTable(intervalos,frequencia,f_acumulada,media,mxf,m2xf): 

    print("\nTabela\n\n-------------------------------------------------------------")

    for i in range(len(intervalos)): 
        print("| " + str(intervalos[i]) + "  |  " + str(frequencia[i]) + "  |  " + str(f_acumulada[i]) + "  |  " + str(media[i]) + "  |  " + str(mxf[i]) + "  |  " + str(m2xf[i]) + "  |  ")

    print("-------------------------------------------------------------------------")

def media_aritmetica(mxf,n): 
    result = 0

    for i in range(len(mxf)): 
        result += mxf[i]

    return result/n

def desvio_padrao(m2xf,n,ma): 
    result = 0

    for i in range(len(m2xf)): 
        result += m2xf[i]

    result -= n * (ma**2)

    result /= n -1 

    return sqrt(result)

def mediana(li, n, faa, fi, h): 
    return li + ((n/2 - faa)/fi) * h

input_string = ""

os = platform.system()
clear_screen = ""

if(os == "Windows" or os == "Darwin"):
    clear_screen = "cls"
else: 
    clear_screen = "clear"

quit = "0"

while ( quit != "-1"):

    tmp = sp.call(clear_screen, shell=True)

    primeiro_intervalo = input("Por favor, insira o primeiro intervalo dos dados separados por espaco :\n(Obs: 0.2 0.6)\n->")

    primeiro_intervalo = list(map(float, primeiro_intervalo.split()))

    opcao = input("O que você possui? A frequência acumulada(0) ou relativa(1)?\n->")


    if(opcao == "0"):
        print("Você escolheu: frequência acumulada")

        f_acumulada = input("Insira os dados:\n-> ")

        f_acumulada = list(map(float, f_acumulada.split()))

        n_rows = len(f_acumulada)
        n_data = f_acumulada[n_rows -1]

        f_absoluta  = frequencia_absoluta(f_acumulada)

        intervalos = intervalos(primeiro_intervalo,n_rows)

        m = media(intervalos)

        mxf = mediaXfrequencia(m,f_absoluta)

        m2xf = media2Xfrequencia(f_absoluta,m)

        s_intervalos = intervalosToString(intervalos)

        printTable(s_intervalos,f_absoluta,f_acumulada,m,mxf,m2xf)

        ma = media_aritmetica(mxf,n_data)

        dv = desvio_padrao(m2xf,n_data,ma)

    elif(opcao == "1"):
        print("Você escolheu: frequência relativa")
    else: 
        print("Opção não existente")

    quit = input("\nQuer sair do programa?\nDigite \'-1\' para sair\nDigite qualquer coisa para continuar\n->")

tmp = sp.call(clear_screen, shell=True)