#Marco Antônio Rudas Napoli, n°USP: 11857970
from tridiagonalULMatrix import *
from tridiagonalSystem import *
from test import *

print('Seja bem vindo ao EP 1 de cálculo numérico')
print('Neste trabalho possuímos duas grandes soluções: \n A primeira é a decomposição LU de uma matriz tridiagonal, enquanto que a segunda é a resolução de um sistema a partir de um matriz tridiagonal cíclica:')
print('Para iniciarmos, escolha um módulo:')
print('(1) Decomposição LU        (2) Resolução de sistemas        (3) Testes Automatizados')
try:
    module = int(input('Insira o módulo: '))
except:
    print('Ocorreu um erro inesperado, verifique os seus dados e tente novamente')

if module != None:
    if module == 1:
        print('\n\n\n\n\n\n')
        firstExercise()
    elif module == 2:
        print('\n\n\n\n\n\n')
        secondExercise()
    elif module == 3:
        print('\n\n\n\n\n\n')
        testAplication()
    else:
        print("Escolha um módulo válido e reinicie o programa")

input()