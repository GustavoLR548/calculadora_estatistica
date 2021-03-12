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

def desvio_padrao(list,ma):
    resultado = 0

    for x in list: 
        resultado += (x - ma)**2

    resultado /= len(list) -1

    return sqrt(resultado)
    
def coeficiente_de_variacao(list,dp,ma):
    return dp/ma*100


input_string = input('Insira os números:\n(Obs: Coloque todos os números separados por espaço)\n->')

number_list = list(map(float, input_string.split()))

print("\nResultado:")

ma = media_aritmetica(number_list)
me = mediana(number_list)
mo = moda(number_list)
dp = desvio_padrao(number_list,ma)
cv = coeficiente_de_variacao(number_list,dp,ma)

print("Media aritmética:        " + str(ma))
print("Mediana:                 " + str(me))
print("Moda:                    " + str(mo))
print("Desvio Padrão:           " + str(dp))
print("Coeficiente de variação: " + str(cv))


