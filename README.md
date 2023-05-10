![logo](https://user-images.githubusercontent.com/82355865/147989422-15a86138-8b0d-4aea-a3c2-1715be570d41.jpg)
# BEECROWD
Aqui você encontra algumas resoluções de problemas do [BEECROWD](https://www.beecrowd.com.br/judge/pt/login). Esses problema pertencem a categoria iniciante, com soluções submetidas na linguagem <b>`python`</b> .

>  <b> Importante⚠️ </b>

🚫 **NÃO copie os códigos. O URI possuiu um sistema que detecta códigos copiados de repositórios online como este.**
**A finalidade deste repositório é ajudar no entendimento da lógica usada no código. Lembre-se de submeter seu próprio código com a sua forma de resolver :smile:.**

#### Problemas disponíveis neste repositório:
*     #1001 Extremamente Básico 
*     #1002 Área do Círculo
*     #1003 Soma Simples
*     #1004 Produto Simples
*     #1005 Média 1
*     #1006 Média 2
*     #1007 Diferença
*     #1008 Salário
*     #1009 Salário com Bônus
*     #1010 Cálculo Simples
*     #1011 Esféra
*     #1012 Área
*     #1013 O Maior
*     #1014 Consumo
*     #1015 Distância Entre Dois Pontos
*     #1016 Distância
*     #1017 Gasto de Combustível
*     #1018 Cédulas
*     #1019 Conversão de Tempo
*     #1020 Idade em Dias
*     #1021 Notas e Moedas
*     #1035 Teste de Seleção 1
*	  #1040 Média 3
* 	  #1041 Coordenadas de um Ponto 
* 	  #1042 Sort Simples


## Notes

# Dicas úteis para competições de programação em Python

Este README contém algumas dicas e recursos úteis para competições de programação em Python.

## Listas de compreensão

Listas de compreensão permitem criar listas a partir de outras listas de maneira mais concisa e elegante. Exemplo:

```
# Criar uma lista com os quadrados de números de 1 a 10
squares = [x**2 for x in range(1, 11)]
```

## `zip()`

A função `zip()` permite iterar sobre várias listas simultaneamente. Exemplo:

```
# Iterar sobre duas listas simultaneamente
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for x, y in zip(list1, list2):
    print(x, y)
```

## Dicionários

Dicionários são úteis para mapear chaves a valores. Exemplo:

```python
# Criar um dicionário que mapeia nomes de frutas a suas cores
fruit_colors = {'banana': 'amarelo', 'maçã': 'vermelho', 'laranja': 'laranja'}
```

## `collections`

O módulo `collections` oferece várias estruturas de dados úteis, como `defaultdict`, `Counter` e `deque`.

## `enumerate()`

A função `enumerate()` é útil para iterar sobre uma lista e obter o índice de cada elemento. Exemplo:

```
# Iterar sobre uma lista e obter o índice de cada elemento
fruits = ['banana', 'maçã', 'laranja']
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

## `sorted()`

A função `sorted()` classifica uma lista em ordem crescente ou decrescente. Exemplo:

```
# Classificar uma lista em ordem crescente
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
```

## `filter()`

A função `filter()` permite filtrar elementos de uma lista com base em uma função de teste. Exemplo:

1. Filtrar apenas os números ímpares de uma lista:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = list(filter(lambda x: x % 2 == 1, numbers))
print(odds) # Output: [1, 3, 5, 7, 9]
```

2. Filtrar apenas os valores booleanos `True` de uma lista:

```python
values = [True, False, True, True, False]
true_values = list(filter(None, values))
print(true_values) # Output: [True, True, True]
```

3. Filtrar apenas as strings com comprimento maior do que 3 em uma lista:

```python
fruits = ['banana', 'maçã', 'laranja', 'uva', 'abacaxi']
long_fruits = list(filter(lambda x: len(x) > 3, fruits))
print(long_fruits) # Output: ['banana', 'maçã', 'laranja', 'abacaxi']
```

4. Filtrar apenas as chaves do dicionário que tenham valor maior do que 100:

```python
prices = {'banana': 50, 'maçã': 75, 'laranja': 90, 'uva': 120, 'abacaxi': 80}
expensive_fruits = list(filter(lambda x: prices[x] > 100, prices))
print(expensive_fruits) # Output: ['uva']
```

5. Filtrar apenas os arquivos com extensão `.txt` em uma lista de nomes de arquivo:

```python
files = ['document.txt', 'image.png', 'presentation.pptx', 'textfile.txt', 'spreadsheet.xlsx']
txt_files = list(filter(lambda x: x.endswith('.txt'), files))
print(txt_files) # Output: ['document.txt', 'textfile.txt']
```

6. Filtrar números pares de uma lista

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

## `map()`

A função `map()` permite aplicar uma função a cada elemento de uma lista. Exemplo:

```
# Elevar ao quadrado cada elemento de uma lista
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))

# Calcular o comprimento de cada string em uma lista:
fruits = ['banana', 'maçã', 'laranja', 'uva']
lengths = list(map(len, fruits))
print(lengths) # Output: [6, 4, 7, 3]



```

## `join()`

O método de string `join()` permite unir elementos de uma lista em uma única string. Exemplo:

```
# Unir elementos de uma lista em uma única string
fruits = ['banana', 'maçã', 'laranja']
fruits_string = ', '.join(fruits)
```

## `set()`

A função `set()` cria um conjunto de elementos únicos. Exemplo:

```python
# Criar um conjunto de números únicos
fruits = {'banana', 'maçã', 'laranja', 'uva', 'abacaxi'}
```
## Ordenação

Python possui diversas funções nativas para ordenação de listas. Seguem abaixo algumas delas:

1. `sorted()`: função que retorna uma nova lista com os elementos ordenados, mantendo a lista original inalterada. Ela pode receber dois argumentos opcionais: `reverse` (para ordenação reversa) e `key` (para definir uma chave de ordenação personalizada).

Exemplo:

```python
numbers = [10, 5, 7, 3, 8, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # Output: [2, 3, 5, 7, 8, 10]
```

2. `list.sort()`: método que ordena a lista original em ordem crescente, sem retornar uma nova lista. Ele também pode receber os argumentos opcionais `reverse` e `key`.

Exemplo:

```python
numbers = [10, 5, 7, 3, 8, 2]
numbers.sort()
print(numbers) # Output: [2, 3, 5, 7, 8, 10]
```

3. `sorted()`, com `key` para ordenação personalizada: podemos passar uma função como argumento `key`, que será aplicada a cada elemento da lista para definir a ordem de ordenação.

Exemplo:

```python
fruits = ['banana', 'maçã', 'laranja', 'uva', 'abacaxi']
sorted_fruits = sorted(fruits, key=len)
print(sorted_fruits) # Output: ['uva', 'maçã', 'banana', 'laranja', 'abacaxi']
```

4. `list.sort()`, com `reverse=True` para ordenação reversa:

Exemplo:

```python
numbers = [10, 5, 7, 3, 8, 2]
numbers.sort(reverse=True)
print(numbers) # Output: [10, 8, 7, 5, 3, 2]
```

5. `max()` e `min()`: funções que retornam o maior e o menor elemento de uma lista, respectivamente.

Exemplo:

```python
numbers = [10, 5, 7, 3, 8, 2]
print(max(numbers)) # Output: 10
print(min(numbers)) # Output: 2
```

6. `sorted()`, com função lambda para ordenação personalizada: podemos usar uma função lambda para definir uma ordem de ordenação personalizada.

Exemplo:

```python
names = ['Ana', 'Lucas', 'Gabriel', 'Maria', 'Pedro']
sorted_names = sorted(names, key=lambda x: x[-1])
print(sorted_names) # Output: ['Lucas', 'Maria', 'Pedro', 'Ana', 'Gabriel']
```

Neste exemplo, a lista `names` é ordenada com base na última letra de cada nome, usando uma função lambda como chave de ordenação personalizada.