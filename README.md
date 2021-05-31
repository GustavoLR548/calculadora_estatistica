# Calculadora estatística

![MIT_LICENSE](https://img.shields.io/badge/license-MIT-green)

Uma simples calculadora em python para fazer calculos de estatística em um grupo de dados

# Como utilizar

Antes de usar o programa, não se esqueça de baixar todos os pacotes necessários para utilizar os programas,
mais especificadamente a instalação do "PrettyTables", biblioteca que usei para formatar o print dos resultados

Para instalar as bibliotecas necessárias, abra o terminal na pasta onde está o ```requirements.txt```, e digite: 

``` pip install -r requirements.txt ``` 

Pronto! Agora apenas vá para a pasta ```src``` e digite no terminal

```python3 agrupados_por_ponto.py``` se você estiver trabalhando com dados agrupados por ponto 

ou

```python3 agrupados_por_intervalo.py``` se você estiver trabalhando com dados agrupados por intervalo

Insira os dados separados espaço e pressione enter. Ou... insira o diretório para um arquivo .csv 

## Exemplo:

```
De onde vêm os dados que você quer inserir? Digite:
 1 - CSV 
 2 - Input
-> 1
Nome do arquivo: 
-> heart.csv -> (arquivo tem que estar no mesmo diretório do arquivo .python)

Resultado:

Tamanho da lista:                 303
---------------------------------------
Maior elemento:                   57
Menor elemento:                 63
---------------------------------------
Ponto Médio:                        60.0
Media aritmética:               54.37
Moda:                                      [58] unimodal
Variância:                              82.48%
Desvio Padrão:                    9.08%
Coeficiente de variação: 16.7%
Quartil:                                 [47.0, 55.0, 61.0]
Outlier superior:                82.0
Outlier inferior:                  26.0

Pressione enter para continuar
```

# Dados a serem imprimidos na tela

## Dados agrupados por ponto

* Número de dados
* Maior e Menor número
* Media aritmética 
* Moda (e o tipo de moda)
* Variância
* Desvio Padrão
* Coeficiente de variação
* 1° Quartil
* Mediana/ 2° Quartil
* 3° Quartil
* Outlier maior
* Outlier menor

## Dados agrupados por intervalo

### No atual momento,é possível calcular usando: 

* Frequência relativa
* Frequência acumulada

E gerar...

* Media aritmética 
* Mediana/ 2° Quartil
* Variância
* Desvio Padrão
* Coeficiente de variação
