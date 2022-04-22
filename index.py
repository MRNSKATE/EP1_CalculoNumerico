from tridiagonalULMatrix import *
from tridiagonalSystem import *

print('Seja bem vindo ao EP 1 de cálculo numérico')
print('Neste trabalho possuímos duas grandes soluções: \n A primeira é a decomposição LU de uma matriz tridiagonal, enquanto que a segunda é a resolução de um sistema a partr de um matriz tridiagonal cíclica:')
print('Para iniciarmos, escolha um módulo:')
print('(1) Decomposição LU        (2) Resolução de sistemas')
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
    