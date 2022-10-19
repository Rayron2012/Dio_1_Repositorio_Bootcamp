# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = int(input())

def calcular_reajuste(salario):
    reajuste = 0

    if salario <= 600:
        reajuste = 17
    elif salario <= 900:
        reajuste = 13
    elif salario <= 1500:
        reajuste = 12
    elif salario <= 2000:
        reajuste = 10
    else:
        reajuste = 5

    return reajuste


reajuste = calcular_reajuste(salario)
parcial = (salario*reajuste) / 100
print(f"Novo salario: {(salario + parcial):.2f}\nReajuste ganho: {parcial:.2f}\nEm percentual: {reajuste} %".replace(".","."))

# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)