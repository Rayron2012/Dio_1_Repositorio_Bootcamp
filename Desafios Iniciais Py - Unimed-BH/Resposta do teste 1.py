# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:
import sys
distancia = int(200)
diametro1 = int(3)
diametro2 = int(8)



icm = distancia / (diametro1 + diametro2)
# icm = int(sys.stdin.readline(distancia / (diametro1 + diametro2)))

print(f"{icm:.2f}")
