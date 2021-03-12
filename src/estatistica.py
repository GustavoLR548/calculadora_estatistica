import collections
import math
from math import sqrt

def media_aritmetica(list):
    soma = 0
    for x in list: 
        soma += x

    return soma/len(list)

def mediana(list):

    list.sort()
    result = 0.0
    size = len(list)
    if(size % 2 == 0):
        result = (list[int(size/2)] + list[int(size/2-1)])/2;
    else:
        result = list[int(size/2)];

    return result;

def moda(list): 
    return ([item for item, count in collections.Counter(list).items() if count > 1])

def variancia(list,ma):
    resultado = 0

    for x in list: 
        resultado += (x - ma)**2

    resultado /= len(list) -1

    return resultado
    
def coeficiente_de_variacao(list,dp,ma):
    return dp/ma*100

def primeiro_quartil(list):
    list.sort()
    result = 0.0
    size = len(list) 
    if(size%2 == 0):
        result = media_aritmetica(list[1:int(size/2-1)])
    else: 
        result = media_aritmetica(list[1:int(size/2)])
    
    return result

def terceiro_quartil(list):
    list.sort()
    result = 0.0
    size = len(list) 
    if(size%2 == 0):
        result = media_aritmetica(list[int(size/2+2):int(size-1)])
    else: 
        result = media_aritmetica(list[int(size/2+1):int(size-1)])
    
    return result


 

input_string = input('Insira os números:\n(Obs: Coloque todos os números separados por espaço)\n->')

number_list = list(map(float, input_string.split()))

print("\nResultado:\n")

ma = media_aritmetica(number_list)
me = mediana(number_list)
mo = moda(number_list)
va = variancia(number_list,ma)
dp = sqrt(va)
cv = coeficiente_de_variacao(number_list,dp,ma)

q1 = primeiro_quartil(number_list)
q3 = terceiro_quartil(number_list)

tipo_de_moda = ""

if (len(mo) == 0):
    tipo_de_moda = "amodal"
elif (len(mo) == 1):
    tipo_de_moda = "unimodal"
elif (len(mo) == 2):
    tipo_de_moda = "bimodal"
else: 
    tipo_de_moda = "multimodal"

print("Media aritmética:        " + str(ma))
print("Mediana/2°Quartil:       " + str(me))
print("Moda:                    " + str(mo) + " " + tipo_de_moda)
print("Variância:               " + str(va) + "%")
print("Desvio Padrão:           " + str(dp) + "%")
print("Coeficiente de variação: " + str(cv) + "%") 

print("Primeiro quartil:        " + str(q1)) 
print("Terceiro quartil:        " + str(q3)) 


