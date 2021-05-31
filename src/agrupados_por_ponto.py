from math import sqrt
import subprocess as sp
import platform
import pandas as pd
import statistics

def media_aritmetica(list):
    soma = 0
    for x in list: 
        soma += x

    return round(soma/len(list),2)

def mediana(list):

    result = 0.0
    size = len(list)
    if(size % 2 == 0):
        result = (list[int(size/2)] + list[int(size/2-1)])/2;
    else:
        result = list[int(size/2)];

    return round(result,2);

def moda(list): 
    ocurrences_of_list_numbers = {}

    for i in list: 
        ocurrences_of_list_numbers.update({i:list.count(i)})

    highest_frequency = max(ocurrences_of_list_numbers.values(), key=float)

    if(highest_frequency == 1):
        return []

    list_of_most_frequent_numbers = []

    for i,j in ocurrences_of_list_numbers.items():
        if(j == highest_frequency):
            list_of_most_frequent_numbers.append(i)

    return list_of_most_frequent_numbers

def variancia(list,ma):
    resultado = 0

    for x in list: 
        resultado += (x - ma)**2

    resultado /= len(list) -1

    return round(resultado,2)
    
def coeficiente_de_variacao(list,dp,ma):
    return round(dp/ma*100,2)

os = platform.system()
clear_screen = ""

if(os == "Windows" or os == "Darwin"):
    clear_screen = "cls"
else: 
    clear_screen = "clear"

quit = "0"


while ( quit != "-1"):

    tmp = sp.call(clear_screen, shell=True)

    entrada = input('De onde vêm os dados que você quer inserir? Digite:\n 1 - CSV \n 2 - Input\n-> ')

    number_list = []

    if('1' in entrada):

        entrada = input('Nome do arquivo: \n-> ')

        data = pd.read_csv(entrada)

        chaves = data.keys()

        for i in chaves:
            number_list.append(list(map(int,data[i])))
    else:

        entrada = input('Digite os dados separados por vírgula: \n-> ')
        number_list.append(list(map(int,entrada.split(','))))

    print("\nResultado:\n")

    for i in number_list:
        ma = media_aritmetica(i)
        me = mediana(i)
        mo = moda(i)
        va = variancia(i,ma)
        dp = round(sqrt(va),2)
        cv = coeficiente_de_variacao(i,dp,ma)

        q = statistics.quantiles(i)

        tipo_de_moda = ""

        if (len(mo) == 0):
            tipo_de_moda = "amodal"
        elif (len(mo) == 1):
            tipo_de_moda = "unimodal"
        elif (len(mo) == 2):
            tipo_de_moda = "bimodal"
        else: 
            tipo_de_moda = "multimodal"

        size = len(i)

        print("Tamanho da lista:        " + str(size))
        print("---------------------------------------")

        print("Maior elemento:          " + str(i[size-1]))
        print("Menor elemento:          " + str(i[0]))
        print("---------------------------------------")
        print("Ponto Médio:             " + str((i[size-1]+i[0])/2))
        print("Media aritmética:        " + str(ma))
        print("Moda:                    " + str(mo) + " " + tipo_de_moda)
        print("Variância:               " + str(va) + "%")
        print("Desvio Padrão:           " + str(dp) + "%")
        print("Coeficiente de variação: " + str(cv) + "%") 
        print("Quartil:                 " + str(q)) 

        print('Outlier superior:        ' + str(q[2] + 1.5*( q[2] - q[0])))
        print('Outlier inferior:        ' + str(q[0] - 1.5*( q[2] - q[0])))

        input('\nPressione enter para continuar')
        tmp = sp.call(clear_screen, shell=True)

    quit = input("\nQuer sair do programa?\nDigite \'-1\' para sair\nDigite qualquer coisa para continuar\n->")


tmp = sp.call(clear_screen, shell=True)