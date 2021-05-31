# Calculadora estatística

![MIT_LICENSE](https://img.shields.io/badge/license-MIT-green)

Uma simples calculadora em python para fazer calculos de estatística em um grupo de dados

# Como utilizar

*UPDATE* 

Antes de usar o programa, não se esqueça de baixar todos os pacotes necessários para utilizar os programas,
mais especificadamente a instalação do "PrettyTables", biblioteca que usei para formatar o print dos resultados

Para instalar as bibliotecas necessárias, abra o terminal na pasta onde está o ```requirements.txt```, e digite: 

``` pip install -r requirements.txt ``` 

Pronto! Agora apenas vá para a pasta ```src``` e digite no terminal

```python3 agrupados_por_ponto.py``` se você estiver trabalhando com dados agrupados por ponto 

ou

```python3 agrupados_por_intervalo.py``` se você estiver trabalhando com dados agrupados por intervalo

Insira os dados separados por vírgula e pressione enter. Ou... insira o diretório para um arquivo .csv (Update :D)

# Dados a serem imprimidos na tela

## Dados agrupados por ponto

* Número de dados
* Maior e Menor número
* Media aritmética 
* Mediana/ 2° Quartil
* Moda (e o tipo de moda)
* Variância
* Desvio Padrão
* Coeficiente de variação
* 1° Quartil
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
