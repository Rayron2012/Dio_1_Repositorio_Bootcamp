carros = ("gol")
print(isinstance(carros, tuple))

# set transforma em unique uma series de informações
print(set(("rayron", "odaleia", "rayron", "me")))


# Union
a = {1, 2}
b = {3, 4}
# union unifica todas as informações com base na união primaria
uni = a.union(b)
print(uni)

# intersection
a = {1, 2, 3}
b = {2, 3, 4}
# intersection unifica o meio dos dados
uni = a.intersection(b)
print(uni)

# diferrence
a = {1, 2, 3}
b = {2, 3, 4}
# diferrence analise a diferença que não tem no outro conjunto exemplo abaixo
uni = a.difference(b) #mostra o que tem de diferente na lista "A" que não tem na b no caso 1
uni2 = b.difference(a) #mostra o que tem de diferente na lista "B" que não tem na b no caso 4
print(uni, uni2)

# symmetric_difference - Faz o mesmo que o anterior so que mais facil
a = {1, 2, 3}
b = {2, 3, 4}
# diferrence analise a diferença que não tem no outro conjunto exemplo abaixo
uni = a.symmetric_difference(b) #mostra o que tem de diferente na lista "A" para lista "B" e da lista B para lista A
print(uni)


letra = 'C'
letra = letra.lower()
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
tam_lista = len(lista)
for i in range(tam_lista):
    if letra in lista:
        x = lista.index(letra)+1

# print(letra.upper())
print(x)

import package_name.file1_name