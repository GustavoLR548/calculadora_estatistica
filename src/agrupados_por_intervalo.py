import subprocess as sp
import platform
from math import sqrt
from prettytable import PrettyTable

def frequencia_absoluta(list): 
    result = []
    result.append(list[0])

    for i in range(len(list)): 
        if (i == 0):
            continue 
        
        result.append(round(list[i] - list[i-1],1))

    return result

def frequencia_acumulada(list): 
    result = []
    acumulador = 0
    for i in range(len(list)): 
        acumulador += list[i]
        result.append(round(acumulador,1))

    return result

def intervalos(list,n):
    interval = list[1] - list[0]  

    for i in range(n):
        if(i == 0):
            continue

        list.append(round(list[i]+interval,1))

    return list

def intervalosToString(list): 
    result = [] 

    for i in range(len(list) - 1): 
        result.append(str(round(list[i],1)) + '-' + str(round(list[i+1],1)))

    return result

def media(list):
    result = [] 

    for i in range(len(list)-1):
        result.append(round((list[i] + list[i+1])/2,1))

    return result

def mediaXfrequencia(f,m):
    result = [] 

    for i in range(len(f)): 
        result.append(round(f[i] * m[i],1))

    return result

def media2Xfrequencia(f,m):
    result = [] 

    for i in range(len(f)): 
        result.append(round(f[i] * (m[i]**2),1))

    return result

def media_aritmetica(mxf,n): 
    result = 0

    for i in range(len(mxf)): 
        result += mxf[i]

    return round(result/n,1)

def desvio_padrao(m2xf,n,ma): 
    result = 0

    for i in range(len(m2xf)): 
        result += m2xf[i]

    result -= n * (ma**2)

    result /= n -1 

    return round(sqrt(result),1)

def mediana(intervalo,f_acumulada,f_absoluta,n): 
    limite = list(map(float, intervalo[int(len(intervalo)/2)].split("-")))

    f_acumulada_anterior = f_acumulada[int(len(f_acumulada)/2-1)]

    f_absoluta_meio = f_absoluta[int(len(f_absoluta)/2)]

    return round(limite[0] + ((n/2 - f_acumulada_anterior) / f_absoluta_meio) * (limite[1] - limite[0]),1)

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

        table = PrettyTable() 

        table.add_column("intervalos", s_intervalos)
        table.add_column("f_absoluta", f_absoluta)
        table.add_column("f_acumulada", f_acumulada)
        table.add_column("x_i", m)
        table.add_column("x_i * f_ab", mxf)
        table.add_column("x_i^2 * f_ab", m2xf)

        print(table)

        ma = media_aritmetica(mxf,n_data)

        dp = desvio_padrao(m2xf,n_data,ma)
        
        me = mediana(s_intervalos,f_acumulada,f_absoluta,n_data)

        print("Media aritmética:        " + str(ma))
        print("Mediana/2°Quartil:       " + str(me))

        print("Variância:               " + str(dp**2) + "%")
        print("Desvio Padrão:           " + str(dp) + "%")
        print("Coeficiente de variação: " + str(dp/ma*100) + "%") 

    elif(opcao == "1"):
        print("Você escolheu: frequência relativa")

        n = int(input("Insira a quantidade de elementos\n->"))

        f_porcentagem = input("Insira os dados(em porcentagem):\n-> ")

        f_porcentagem = list(map(float, f_porcentagem.split()))

        f_absoluta = []

        for i in range(len(f_porcentagem)):
            f_absoluta.append(round((f_porcentagem[i] / 100) * n))

        f_acumulada = frequencia_acumulada(f_absoluta)

        intervalos = intervalos(primeiro_intervalo,len(f_porcentagem))

        m = media(intervalos)

        mxf = mediaXfrequencia(m,f_absoluta)

        m2xf = media2Xfrequencia(f_absoluta,m)

        s_intervalos = intervalosToString(intervalos)

        table = PrettyTable() 

        table.add_column("intervalos", s_intervalos)
        table.add_column("f_absoluta", f_absoluta)
        table.add_column("f_acumulada", f_acumulada)
        table.add_column("x_i", m)
        table.add_column("x_i * f_ab", mxf)
        table.add_column("x_i^2 * f_ab", m2xf)

        print(table)

        ma = media_aritmetica(mxf,n)

        dp = desvio_padrao(m2xf,n,ma)
        
        me = mediana(s_intervalos,f_acumulada,f_absoluta,n)

        print("Media aritmética:        " + str(ma))
        print("Mediana/2°Quartil:       " + str(me))

        print("Variância:               " + str(dp**2) + "%")
        print("Desvio Padrão:           " + str(dp) + "%")
        print("Coeficiente de variação: " + str(round(dp/ma*100,1)) + "%") 

    else: 
        print("Opção não existente")

    quit = input("\nQuer sair do programa?\nDigite \'-1\' para sair\nDigite qualquer coisa para continuar\n->")

tmp = sp.call(clear_screen, shell=True)